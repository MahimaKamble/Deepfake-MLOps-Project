pipeline {
agent any

```
stages {

    stage('Deploy with Ansible') {
        steps {
            bat '''
            wsl bash -c "cd /home/mahima/ansible-project && ansible-playbook -i inventory.ini deploy_real.yml"
            '''
        }
    }
}
```

}
