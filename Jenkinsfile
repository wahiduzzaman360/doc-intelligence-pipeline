pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                sh 'docker build -t doc-intelligence-backend:latest ./backend'
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                sh 'docker build -t doc-intelligence-frontend:latest ./frontend'
            }
        }
    }
}