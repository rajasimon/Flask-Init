import os
import click
import flask_init
from jinja2 import Environment, PackageLoader


def creator(project_type, project_path):
    click.echo(project_type)
    click.echo(project_path)
    module_path = os.path.join(
        os.path.dirname(flask_init.__file__), project_type
    )

    # Initialize the jinja2 environment variable
    environment = Environment(
        loader=PackageLoader('flask_init', project_type))

    for temp in environment.list_templates():

        template = environment.get_template(temp)
        
        # Apply context
        parsed_template = template.render()

        # Remove tpl in the name
        file_name = template.name.split('-tpl')[0]
        distination_file = os.path.join(project_path, file_name)
        
        # Create folder if no folder in that distination folder
        # https://stackoverflow.com/a/12517490/3762142
        if not os.path.exists(os.path.dirname(distination_file)):
            os.makedirs(os.path.dirname(distination_file))

        with open(distination_file, "w") as f:
            f.write(parsed_template + '\n')
