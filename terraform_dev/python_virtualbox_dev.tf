terraform {
  required_providers {
    vagrant = {
      source = "bmatcuk/vagrant"
      version = "~> 4.0.0"
    }
  }
}

resource "vagrant_vm" "timeserver_python_dev_vm" {
  vagrantfile_dir = "../vagrant_dev/"
  env = {}
  get_ports = true
}

