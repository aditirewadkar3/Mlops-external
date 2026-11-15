
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:/Users/Aditi/AppData/Local/Programs/Python/Python311/python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Addition') {
            steps {
                bat '"C:/Users/Aditi/AppData/Local/Programs/Python/Python311/python.exe" -c "print(12 + 20)"'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '"C:/Users/Aditi/AppData/Local/Programs/Python/Python311/python.exe" -m pytest -v'
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
