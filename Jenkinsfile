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
        "C:\\Python314\\python.exe" -m venv venv
        call venv\\Scripts\\activate
        python -m pip install --upgrade pip
            '''
    }
}

     stage('Run API Tests') {
    steps {
        bat '''
        call venv\\Scripts\\activate
        pytest --junitxml=test-results/results.xml
        '''
    }
}

    post {
        always {
            // Archives test results in Jenkins
            junit 'results.xml'
        }
    }
}
}
