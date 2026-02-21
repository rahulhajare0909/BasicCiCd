pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/rahulhajare0909/BasicCiCd.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Code Quality') {
            steps {
                sh 'pylint app --fail-under=6'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests --html=report.html'
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}
