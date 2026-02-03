pipeline {
    agent any

    environment {
        IMAGE_NAME = "devsecops-app"
        SONAR_HOST_URL = "http://192.168.80.130:9000"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withCredentials([
                    string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')
                ]) {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=devsecops-Project \
                      -Dsonar.sources=src \
                      -Dsonar.host.url=${SONAR_HOST_URL} \
                      -Dsonar.login=${SONAR_TOKEN} \
                      -Dsonar.python.version=3.9
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh '''
                trivy image \
                  --severity HIGH,CRITICAL \
                  --exit-code 0 \
                  ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }

        stage('Terraform Provisioning') {
            steps {
                dir('terraform') {
                    sh '''
                    terraform init
                    terraform apply -auto-approve
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ DevSecOps pipeline completed successfully"
        }
        failure {
            echo "❌ Pipeline failed — check logs"
        }
    }
}
