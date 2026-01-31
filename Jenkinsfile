pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                echo 'Cloning repository'
                git branch: 'main',
                    url: 'https://github.com/your-username/devsecops-project.git'
            }
        }
    }
}
