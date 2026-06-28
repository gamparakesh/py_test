pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pulls the latest code from your repo
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Creates a virtual environment and installs requirements
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                // Executes your pytest regression suite
                bat '''
                call venv\\Scripts\\activate
                pytest --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            // Archives test results in Jenkins
            junit 'results.xml'
        }
    }
}
