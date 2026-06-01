pipeline {
agent any

stages {

    stage('Deploy with Ansible') {
        steps {
            bat '''
            C:\\Windows\\System32\\wsl.exe bash -c "cd /home/mahima/ansible-project && ansible-playbook -i inventory.ini deploy_real.yml"
            '''
        }
    }
}

}

# Jenkins