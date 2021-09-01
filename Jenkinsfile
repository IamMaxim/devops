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
            app = docker.build("getintodevops/hellonode")
        }

        stage('Push image') {
            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                app.push("latest")
            }
        }
    }
}