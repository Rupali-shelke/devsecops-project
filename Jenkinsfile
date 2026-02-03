pipeline {
    agent any

    environment {
        IMAGE_NAME = "devsecops-app"
        DOCKERHUB_CREDENTIALS = "dockerhub"      // Jenkins credentials ID for Docker Hub (Username/Password type)
        DOCKERHUB_REPO = "rupalishelake/devsecops-project" // Replace with your Docker Hub username/repo
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
                    --exit-code 0 \
                    ${IMAGE_NAME}:${BUILD_NUMBER}
                """
            }
        }

        stage('Docker Push') {
            steps {
                echo "🔹 Pushing Docker image to Docker Hub"
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${DOCKERHUB_REPO}:${BUILD_NUMBER}
                    docker push ${DOCKERHUB_REPO}:${BUILD_NUMBER}
                    """
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
