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

        stage('Load Images into Minikube') {
            steps {
                sh 'minikube image load doc-intelligence-backend:latest'
                sh 'minikube image load doc-intelligence-frontend:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/'
            }
        }

        stage('Verify Kubernetes Rollout') {
            steps {
                sh 'kubectl rollout status deployment/backend-deployment --timeout=120s'
                sh 'kubectl rollout status deployment/frontend-deployment --timeout=120s'
            }
        }
    }
}
