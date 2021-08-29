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

## TerraForm best practices
- Use workspace to isolate project from other resources.
