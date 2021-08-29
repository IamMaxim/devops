# Terraform for Time Server

`virtualbox_vm` provider is used for local Terraform deployment.

---

Since TerraForm... let's say, has a VERY poor support for VirtualBox (the provider never escaped ALPHA version), I decided to use Vagrant provider for TerraForm to create VirtualBox VM.

> To use Vagrant without TerraForm, you may execute this from the root of repository:
> 
> ```shell
> cd vagrant
> vagrant up && vagrant provision
> ```

To use TerraForm, run from the root of repository:

```shell
cd terraform
terraform init
terraform apply
```

## Setting up development environment using Terraform

Setting up development environment is tedious task, so Terraform configuration for Time Server app is present in the `terraform_dev` directory. Run:

```shell
cd terraform_dev
terraform init
terraform apply
```

to get server running on your machine. `app_python` directory is synced to the VM, so all your changes to Python files will be reflected in runtime in less a second.

## TerraForm best practices
- Use workspaces to isolate project from other resources.
