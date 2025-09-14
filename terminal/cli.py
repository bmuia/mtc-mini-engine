import click
from terminal.main import Zapper

@click.group()
def cli():
    """Zapper CLI"""
    pass

@click.command('register')
def call_register():
    zipp = Zapper()
    zipp.openbrowserregister('http://localhost:8000/register/')

@click.command('login')
def call_login():
    zipp = Zapper()
    zipp.openbrowserlogin('http://localhost:8000/login/')


cli.add_command(call_register)
cli.add_command(call_login)

if __name__ == '__main__':
    cli()
