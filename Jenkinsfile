
pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                echo 'Cloning repository'
                git branch: 'main',
                    url: 'https://github.com/Rupali-shelke/devsecops-project.git'
            }
        }
    }
}

