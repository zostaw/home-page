#!groovy
pipeline {


    tools {nodejs "node"}

    environment {
        IMAGE_NAME = "zostaw/home-page"
        IMAGE_TAG = "python-app-1.0.0"
        dockerhub = credentials("dockerhub")
        sshkey = credentials("file_octojenkssh")
    }
    agent {
        kubernetes {
            // Rather than inline YAML, in a multibranch Pipeline you could use: yamlFile 'jenkins-pod.yaml'
            // Or, to avoid YAML:
            // containerTemplate {
            //     name 'shell'
            //     image 'ubuntu'
            //     command 'sleep'
            //     args 'infinity'
            // }
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
            // Can also wrap individual steps:
            // container('shell') {
            //     sh 'hostname'
            // }
            defaultContainer 'shell'
        }
    }

      stages {
        stage('Pre script') {
            steps {
                sh 'pwd'
                sh 'ls -las'
                sh 'apk --update add bash vim g++ gcc musl-dev linux-headers'
                sh 'pip install --upgrade pip'
                sh 'pip install --no-cache-dir -r ./requirements.txt'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python HomePage.py start &'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
                container("docker"){
                    sh 'hostname'
                    sh 'pwd'
                    sh 'ls -las'
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
cat <<EOF > ./create_home_page.yaml
apiVersion: v1
kind: Pod
metadata:
  name: home-page
spec:
  containers:
  - name: home-page
    image: $IMAGE_NAME:$IMAGE_TAG
    ports:
    - containerPort: 33000
"
'''
                    sh 'ssh -o StrictHostKeyChecking=no -i /tmp/secret zostaw@192.168.0.172 "/usr/bin/microk8s kubectl apply -f ./create_home_page.yaml"'
                }
              }
        }
    }

}
