pipeline {
    agent {
        docker {
            image 'python:3.9.6-bullseye'
            args '-u root:root'
        }
    }
    stages {
        stage('checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'cd app_python && pip install -r requirements.txt'
                sh 'cd app_python/src && python manage.py test'
            }
        }

        stage('Build and push Docker image') {
            withCredentials([[
                $class: 'UsernamePasswordMultiBinding',
                credentialsId: params.JP_DockerMechIdCredential,
                usernameVariable: 'DOCKER_LOGIN',
                passwordVariable: 'DOCKER_PASSWORD'
            ]]) {
                usr = USERNAME
                pswd = PASSWORD
            }

            docker.withRegistry("https://registry.hub.docker.com", params.JP_DockerMechIdCredential) {
                sh "docker login -u ${usr} -p ${pswd}"
                def	image = docker.build("iammaxim/devops")
                image.push 'latest'
            }
        }
    }
}