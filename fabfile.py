from fabric.api import env, roles, run, cd

# Define sets of servers as roles
env.roledefs = {
    'web': ['zooeyherself.dreamhosters.com'],
}

# Set the user to use for ssh
env.user = 'zoring'


@roles('web')
def deploy():
    with cd('~/zooeyherself.com'):
        run('git checkout master')
        run('git pull zoing master')
