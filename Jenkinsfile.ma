pipeline {
    agent any
    parameters {
        file(name: 'FILE_TO_DOWNLOAD', description: 'Upload export.csv file')
    }
    stages {
        stage('Download File') {
            steps {
                script {
                    def workspacePath = pwd()
                    def downloadedFilePath = "${workspacePath}/${params.FILE_TO_DOWNLOAD}"
                    sh "mv ${downloadedFilePath} ./export.csv"
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
