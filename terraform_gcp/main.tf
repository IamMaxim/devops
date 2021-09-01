// Configure the Google Cloud provider
provider "google" {
  credentials = file("../gcp_key.json")
  project = "ultra-brand-146520"
  region = "us-central1"
  zone = "us-central1-a"
}

// Terraform plugin for creating random ids
resource "random_id" "instance_id" {
  byte_length = 8
}

// A single Compute Engine instance
resource "google_compute_instance" "default" {
  // Google provides 1 free e2-micro in certain US regions, so we use it here.
  name = "devops-vm"
  machine_type = "e2-micro"
  zone = "us-central1-a"
  tags = [
    "devops-node"
  ]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Include this section to give the VM an external ip address
    }
  }

  metadata = {
    ssh-keys = "root:${file("${var.public_key_path}")}"
  }

  provisioner "remote-exec" {
    connection {
      type = "ssh"
      user = "root"
      private_key = file("${var.private_key_path}")
      agent = false
      host = google_compute_instance.default.network_interface[0].access_config[0].nat_ip
    }

    inline = [
      "sudo curl -sSL https://get.docker.com/ | sh",
      "sudo usermod -aG docker `echo $USER`",
      "sudo docker run -d -p 80:8000 iammaxim/devops"
    ]
  }

  service_account {
    scopes = [
      "https://www.googleapis.com/auth/compute.readonly"
    ]
  }
}

resource "google_compute_firewall" "default" {
  name = "devops-firewall"
  network = "default"

  allow {
    protocol = "tcp"
    ports = [
      "80"
    ]
  }

  source_ranges = [
    "0.0.0.0/0"
  ]
  target_tags = [
    "devops-node"
  ]
}