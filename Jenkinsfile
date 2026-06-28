pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
               bat '''
        "C:\\Python314\\python.exe" -m venv venv
        call venv\\Scripts\\activate
        python -m pip install --upgrade pip
        python -m pip install pytest
        '''
            }
        }

        stage('Run API Tests') {
            steps {
                bat '''
                mkdir test-results
                call venv\\Scripts\\activate
                pytest --junitxml=test-results/results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'test-results/results.xml'
        }
    }
}
