pipeline {
    agent any
    parameters {
        file(name: 'export.csv', description: 'Upload export.csv file')
    }
    stages {
        stage('checkout code') {
            steps{
                checkout scm
            }
        }
        stage('MikroTik') {
            steps {
                catchError {
                sh 'python3 mikrotik_availability.py'
                }
                echo currentBuild.result
            }
        }
   }
}
