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

        stage('Build Docker image') {
            steps {
                def	image = docker.build("iammaxim/devops")
            }
        }

        stage('Push Docker image') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-hub-credentials',
                        usernameVariable: 'DOCKER_LOGIN',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    docker.withRegistry('', 'docker-hub-credentials') {
                        sh "docker login -u ${USERNAME} -p ${PASSWORD}"
                        image.push("latest")
                    }
                }
            }
        }
    }
}