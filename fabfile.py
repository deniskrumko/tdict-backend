import subprocess

from fabric.api import local, task
from fabric.operations import prompt

# MAIN COMMANDS
# ============================================================================


@task
def manage(command):
    """Run ``python3 manage.py`` command."""
    return local('python3 manage.py {}'.format(command))


@task
def remote(host='192.168.1.11', port=8000):
    """Run remove server."""
    ifconfig = subprocess.check_output('ifconfig')
    if host not in ifconfig.decode('utf-8'):
        return print(f'Host {host} not in "ifconfig"', error=True)

    return manage(f'runserver {host}:{port}')


@task
def run():
    """Run server"""
    return manage('runserver')


@task
def shell():
    """Run python shell."""
    return manage('shell')


@task
def startapp(app_name):
    """Start new application.

    Name of application can be nested, like "apps.app_name" or
    "apps.utils.app_name".

    """
    names_list = app_name.split('.')

    if len(names_list) == 1:
        return print(
            'Name of app must include root folder. '
            'Like "apps.{}"'.format(names_list[0]),
            error=True,
        )

    path = '/'.join(names_list)
    local('mkdir {0}'.format(path))
    manage(
        'startapp --template=core/app_template {0} {1}'
        .format(names_list[-1], path),
    )
    return print('Please, add your app to "INSTALLED_APPS"')


# GIT
# ============================================================================

@task
def push():
    """Push changes to all servers."""
    print('1. Pushing to origin')
    local('git push origin master --tags')

    print('2. Pushing to Heroku')
    local('git push heroku master')


# MIGRATIONS AND DATABASE
# ============================================================================

@task
def makemigrations():
    """Make migrations for database."""
    manage('makemigrations')


@task
def migrate():
    """Apply migrations to database."""
    print('Applying migrations')
    manage('migrate')


@task
def createsuperuser(email='root@root.ru'):
    """Create superuser with default credentials."""
    print('Creating superuser')
    return manage('createsuperuser --username root --email {}'.format(email))


@task
def resetdb():
    """Reset database to initial state."""
    print('Remove "scr/media" folder')
    local('rm -rf media/')

    print('Reset database')
    manage('reset_db -c --noinput')

    migrate()
    createsuperuser()

    print('Populate database?')
    answer = prompt('\n', default='yes')

    if answer.lower() in ('y', 'yes', 1):
        populate_db()


# STATIC CHECKS: ISORT AND PEP8
# ============================================================================

@task
def isort():
    """Fix imports formatting."""
    print('Running imports fix')
    local('isort apps core config')


@task
def pep8(path='apps core'):
    """Check PEP8 errors."""
    print('Checking PEP8 errors')
    return local('flake8 --config=.flake8 {}'.format(path))


# HEROKU
# ============================================================================

@task
def hlogs():
    """Get Heroku logs."""
    local('heroku logs --source app --tail')


# MANAGEMENT COMMANDS SHORTCUTS
# ============================================================================

@task
def populate_db():
    """Populate database with dummy data."""
    print('NOT YET IMPLEMENTED')
