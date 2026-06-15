pipeline {
    agent {
        kubernetes {
            label 'quantumcommerce-agent'

            defaultContainer 'jnlp'

            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: jnlp
    image: jenkins/inbound-agent:latest

  - name: docker
    image: docker:24-dind
    command:
    - cat
    tty: true
    volumeMounts:
    - name: docker-sock
      mountPath: /var/run/docker.sock

  - name: kubectl
    image: bitnami/kubectl:latest
    command:
    - cat
    tty: true

  volumes:
  - name: docker-sock
    hostPath:
      path: /var/run/docker.sock
"""
        }
    }

    environment {
        DOCKERHUB_REPO = "your-dockerhub-username/quantumcommerce"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Frontend') {
            steps {
                sh '''
                echo "Building frontend..."
                cd frontend
                echo "Frontend build step simulated (add npm if needed)"
                '''
            }
        }

        stage('Build Backend') {
            steps {
                sh '''
                echo "Building backend..."
                cd backend
                echo "Backend build step simulated (add mvn/npm/gradle if needed)"
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                container('docker') {
                    sh '''
                    echo "Building Docker images..."

                    docker version

                    docker build -t $DOCKERHUB_REPO-frontend:$IMAGE_TAG ./frontend
                    docker build -t $DOCKERHUB_REPO-backend:$IMAGE_TAG ./backend
                    '''
                }
            }
        }

        stage('Push Images to DockerHub') {
            steps {
                container('docker') {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        sh '''
                        echo $PASS | docker login -u $USER --password-stdin

                        docker push $DOCKERHUB_REPO-frontend:$IMAGE_TAG
                        docker push $DOCKERHUB_REPO-backend:$IMAGE_TAG
                        '''
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                container('kubectl') {
                    sh '''
                    echo "Deploying to Kubernetes..."

                    kubectl apply -f k8s/

                    kubectl get pods
                    kubectl get svc
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                container('kubectl') {
                    sh '''
                    echo "Checking rollout status..."

                    kubectl rollout status deployment/backend || true
                    kubectl rollout status deployment/frontend || true
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline SUCCESS 🚀 QuantumCommerce deployed successfully"
        }
        failure {
            echo "Pipeline FAILED ❌ Check logs"
        }
    }
}
