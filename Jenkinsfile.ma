pipeline {
    agent any
    parameters {
        file(name: 'FILE_TO_DOWNLOAD', description: 'Upload export.csv file')
    }
    stages {
        stage('checkout code') {
            steps{
                deleteDir()
                checkout scm
            }
        }
        stage('Download File') {
            steps {
                script {
                    def downloadedFilePath = params.FILE_TO_DOWNLOAD
                    sh "cp ${downloadedFilePath} ./export.csv"
                }
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
