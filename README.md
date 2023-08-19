# learning_jenkins_pipeline
This repository creates base docker image for my home-page.

# Usage

The following section specifies how to build and send to docker hub a multi-arch docker images with python dependencies for home-page.

```bash
DOCKER_NAME="zostaw/multiarch-numpy-base"
DOCKER_TAG="buildx-latest"
DOCKER_TAG_SHA="$(date | shasum -a 256 | awk '{print $1}')"
# enter credentials to send to github
docker login
# use desktop-linux for multiplatform emulation
docker buildx create --use desktop-linux
docker buildx build --push --platform linux/arm/v6,linux/arm64,linux/arm/v8,linux/amd64 --tag ${DOCKER_NAME}:${DOCKER_TAG} --tag ${DOCKER_NAME}:${DOCKER_TAG_SHA} .
```

