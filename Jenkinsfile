pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Rupali-shelke/devsecops-project.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    sonar-scanner \
                    -Dsonar.projectKey=devsecops-Project \
                    -Dsonar.sources=src
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devsecops-app:${BUILD_NUMBER} .'
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh '''
                trivy image \
                --severity HIGH,CRITICAL \
                --exit-code 0 \
                devsecops-app:${BUILD_NUMBER}
                '''
            }
        }

	stage('Fetch Secrets from Vault') {
            steps {
                withVault([vaultSecrets: [[
                    path: 'secret/app',
                    secretValues: [
                        [envVar: 'DB_PASSWORD', vaultKey: 'db_password']
                    ]
                ]]]) {
                    sh '''
                      echo "Vault secret fetched successfully"
                      # Secret is used internally, not printed
                    '''
                }
            }
        }
	stage('Terraform Provisioning') {
            steps {
                sh '''
                  terraform init
                  terraform apply -auto-approve
                '''
            }
        }
    
    }    
}
