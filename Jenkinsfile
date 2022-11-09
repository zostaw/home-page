#!groovy
pipeline {


    tools {nodejs "node"}

    environment {
        IMAGE_NAME = "zostaw/home-page"
        IMAGE_TAG = "tst-1.0.1"
        dockerhub = credentials("dockerhub")
        sshkey = credentials("file_octojenkssh")
    }
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: shell
    image: zostaw/numpy:python-numpy-1.0
    command:
    - sleep
    args:
    - infinity
    tty: true
    volumeMounts:
      - mountPath: /var/run/docker.sock
        name: docker-sock
  - name: docker
    image: docker:20.10.21-alpine3.16
    command:
    - cat
    tty: true
    volumeMounts:
      - mountPath: /var/run/docker.sock
        name: docker-sock
  - name: ssh
    image: jenkins/ssh-agent:alpine
    command:
    - sleep
    args:
    - infinity
  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
'''
            defaultContainer 'shell'
        }
    }

      stages {
        stage('Pre script') {
            steps {
                sh 'pwd'
                sh 'ls -las'
                sh 'cat .git/config'
                sh 'apk --update add bash vim g++ gcc musl-dev linux-headers'
                sh 'pip install --upgrade pip'
                sh 'pip install --no-cache-dir -r ./requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'hostname'
                sh 'pwd'
                sh 'ls -las'
                sh 'python HomePage.py start &'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                container("docker"){
                    sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
                    sh 'echo ${dockerhub_PSW} | docker login -u="${dockerhub_USR}" --password-stdin'
                    sh 'docker image push $IMAGE_NAME:$IMAGE_TAG'
                }
            }
        }
          stage('Deploy'){
              steps{
                  container('ssh'){
                    sh 'cat ${sshkey} > /tmp/secret && chmod 0600 /tmp/secret'
                    sh '''ssh -o StrictHostKeyChecking=no -i /tmp/secret zostaw@192.168.0.172 "
cat <<EOF > /tmp/pod_home_page_tst.yaml
apiVersion: v1
kind: Pod
metadata:
  name: home-page-tst
  namespace: default
  labels:
    app.kubernetes.io/name: home-page-tst
spec:
  containers:
  - name: home-page-tst
    image: $IMAGE_NAME:$IMAGE_TAG
    ports:
    - containerPort: 8080
EOF
cat <<EOF > /tmp/service_home_page_tst.yaml
apiVersion: v1
kind: Service
metadata:
  name: home-page-tst
  namespace: default
  labels:
    app.kubernetes.io/name: home-page-tst
spec:
  selector:
    app.kubernetes.io/name: home-page-tst
  type: NodePort
  ports:
    - port: 8080
      targetPort: 8080
      nodePort: 30001
EOF
/usr/bin/microk8s kubectl replace --force -f /tmp/pod_home_page_tst.yaml
/usr/bin/microk8s kubectl replace --force -f /tmp/service_home_page_tst.yaml
                    "'''
                }
              }
        }
    }

}
