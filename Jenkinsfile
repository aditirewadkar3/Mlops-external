
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                dir('C:/B.tech Final/MLops external POE') {
                    bat 'python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Addition') {
            steps {
                dir('C:/B.tech Final/MLops external POE') {
                    bat 'python -c "print(12 + 20)"'
                }
            }
        }

        stage('Run Pytest') {
            steps {
                dir('C:/B.tech Final/MLops external POE') {
                    bat 'python -m pytest -v'
                }
            }
        }
    }

    post {
        success {
            echo 'Addition project executed successfully!'
        }

        failure {
            echo 'Build failed!'
        }
    }
}
