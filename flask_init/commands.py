import os
import click
import flask_init
from flask_init.helper import creator

# Project type
simple_module_name = 'templates/simple'
single_module_name = 'templates/single_module'


@click.command()
@click.argument('project-name')
@click.option('--simple', is_flag=True)
@click.option('--single-module', is_flag=True)
@click.option('--package', is_flag=True)
@click.option('--blueprints', is_flag=True)
def cli(project_name, simple, single_module, package, blueprints):
    """
    Easy way to create Flask Web application. You can use below option with flask init::
        
        --simple-module
        --single-module
    """
    project_path = None

    if project_name:
        if simple or single_module or package or blueprints:
            project_path = os.path.join(os.getcwd(), project_name)
            if not os.path.isdir(project_path):
                os.mkdir(project_path)

    if single_module:
        creator(single_module_name, project_path)

    else:
        creator(simple_module_name, project_path)
        