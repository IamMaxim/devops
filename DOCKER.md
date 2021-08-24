# Docker configuration

`app_python` directory contains `Dockerfile` that builds app image and `build_docker.sh` script as a shorthand for
running `docker build` with `latest` tag.

Official Python docker image is used as a base for this image.

Repository root contains `docker-compose` file to startup the project with all parameters.

## Best practices

- The Docker image does not use root as user, lowering the privileges of potentially malicious Python code.
- Exposed ports are marked in Dockerfile, so other images like automated NGINX proxy may take advantage of this.
- Only source folder is copied, leaving unnecessary files away.
- Metadata is added to the Dockerfile.
- docker-compose file is added to the root of repository, showing the example of usage.
