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
                sh 'cd src && python manage.py test'
//                 junit 'nosetests.xml'
//                 cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
            }
        }
//         stage('Lint') {
//             steps {
//                 sh 'pipenv run lint'
//                 warnings canResolveRelativePaths: false, canRunOnFailed: true, categoriesPattern: '', consoleParsers: [[parserName: 'PyLint']], defaultEncoding: '', excludePattern: '', healthy: '', includePattern: '', messagesPattern: '', unHealthy: ''
//             }
//         }
    }
}