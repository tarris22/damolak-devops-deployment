pipeline {
    agent any

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies and Test') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pip install pytest'
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Docker build stage prepared; execution will be enabled later.'
                // Enable after Docker is installed and configured on the Jenkins agent.
                // bat 'docker build -t devops-practical-challenge:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment is not enabled yet. AWS setup and cost review are required.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Review the stage logs above.'
        }
        always {
            echo 'Pipeline run finished.'
        }
    }
}
