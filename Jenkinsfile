pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Repository checked out by Jenkins.'
            }
        }

        stage('Install Dependencies and Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt pytest
                    python -m pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-practical-challenge:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment is pending AWS configuration.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Review the stage logs.'
        }
        always {
            echo 'Pipeline run finished.'
        }
    }
}
