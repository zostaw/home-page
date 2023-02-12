# home-page

This is source code for my personal home page.

It is deployed as docker image and it runs by default on port 8080.

In below instruction, the following $IMAGE_NAME:$IMAGE_TAG refers to docker image you'll be using, you MUST replace it with correct image version.
Simply replace "$IMAGE_NAME:$IMAGE_TAG" below with "zostaw/home-page:app-1.0.1".

## PREREQUISITES

- docker

## INSTALLATION

### Setup

1. Pull submodules:

```
git submodule init
git submodule update
```

2. setup https

    a. generate certificate (cert.pem, key.pem), for example (self-signed):
    ```bash
    openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    ```

    b. place in app directory:
    ```bash
    app/cert.pem
    app/key.pem
    ```

## START

### Standalone

```bash
python HomePage.py start # optionally add "--ssl_mode=http"
```

### Docker

```bash
docker build -t $IMAGE_NAME:$IMAGE_TAG .
docker run --name=home-page $IMAGE_NAME:$IMAGE_TAG
```

### Kubernetes

1. create pod-home-page.yaml

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: home-page
      namespace: default
      labels:
        app.kubernetes.io/name: home-page
    spec:
      containers:
      - name: home-page
        image: $IMAGE_NAME:$IMAGE_TAG
        imagePullPolicy: Always
        ports:
        - containerPort: 8080
    ```

2. create service-home-page.yaml to expose pod outside cluster

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: home-page
      namespace: default
      labels:
        app.kubernetes.io/name: home-page
    spec:
      selector:
        app.kubernetes.io/name: home-page
      type: NodePort
      ports:
        - port: 8080
          targetPort: 8080
          nodePort: <your port>
    ```
