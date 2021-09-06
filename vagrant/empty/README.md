# Empty Vagrant VM

The name tells it all. It is just a virgin Ubuntu VM with password-enabled SSH login.
Default credentials are root:root.

You can use it with:
```shell
ssh -p 2222 root@127.0.0.1
```

If VM does not start up, install VB Guest additions plugin:
```shell
vagrant plugin install vagrant-vbguest
```
