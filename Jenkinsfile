pipeline {
    agent any

    environment {
        IMAGE_NAME = "devsecops-app"
        SONAR_HOST_URL = "http://192.168.80.130:9000"
    }

    stages {

        stage('Docker Build') {
            steps {
                echo "🔹 Building Docker image"
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} src/"
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonarqube-token', variable: 'SONAR_TOKEN')]) {
                    echo "🔹 Running SonarQube Scanner"
                    sh """
                    sonar-scanner \
                        -Dsonar.projectKey=devsecops-Project \
                        -Dsonar.sources=src \
                        -Dsonar.host.url=${SONAR_HOST_URL} \
                        -Dsonar.login=${SONAR_TOKEN} \
                        -Dsonar.python.version=3.9
                    """
                }
            }
        }

        stage('Trivy Image Scan') {
            steps {
                echo "🔹 Scanning Docker image for vulnerabilities"
                sh """
                trivy image \
                    --severity HIGH,CRITICAL \
                    --exit-code 1 \
                    ${IMAGE_NAME}:${BUILD_NUMBER}
                """
            }
        }

        stage('Terraform Provisioning') {
            steps {
                dir('terraform') {
                    echo "🔹 Initializing Terraform"
                    sh "terraform init"
                    echo "🔹 Planning Terraform changes"
                    sh "terraform plan -out=tfplan"
                    echo "🔹 Applying Terraform changes"
                    sh "terraform apply -auto-approve tfplan"
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
