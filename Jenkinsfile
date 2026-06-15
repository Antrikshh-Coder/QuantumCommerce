pipeline {
    agent any

    environment {
        APP_NAME = "quantumcommerce"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/Antrikshh-Coder/QuantumCommerce.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                docker build -t quantumcommerce-frontend ./frontend
                docker build -t quantumcommerce-backend ./backend
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl get pods
                kubectl get svc
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD Pipeline SUCCESS 🚀"
        }
        failure {
            echo "Pipeline FAILED ❌"
        }
    }
}
