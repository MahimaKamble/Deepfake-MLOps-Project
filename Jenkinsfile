pipeline {
    agent any

    stages {

        stage('Test EC2 Connection') {
            steps {
                sshagent(credentials: ['ec2-key']) {
                    bat '''
                    ssh -o StrictHostKeyChecking=no ec2-user@51.21.169.193 "hostname"
                    '''
                }
            }
        }
    }
}