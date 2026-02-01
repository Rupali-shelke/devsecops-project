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
                    -Dsonar.projectKey=devsecops-project \
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
    }
}
