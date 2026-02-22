pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/rahulhajare0909/BasicCiCd.git', branch: 'main'
            }
        }

        stage('Setup Python') {
            steps {
                bat '"C:\\Users\\VICTUS\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }
    }
}
