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
        bat '''
        "C:\\Users\\lilly\\AppData\\Local\\Programs\\Python\\Python314\\python.exe" -m venv venv
        call venv\\Scripts\\activate
        python -m pip install --upgrade pip
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
