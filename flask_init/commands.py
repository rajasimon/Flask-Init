import click
from jinja2 import Environment, PackageLoader


@click.command()
def cli():
    """
    Easy way to create Flask Web application.
    """
    env = Environment(loader=PackageLoader('flask_init', 'templates'))

    # Get the templates
    template = env.get_template('app.py-tpl')

    # Apply context
    parsed_template = template.render()

    # Remove tpl in the name
    file_name = template.name.split('-tpl')[0]
    with open(file_name, "w") as f:
        f.write(parsed_template + '\n')

    # Notify user about the file
    click.echo('Flask app.py file generated. Use below command to run.')
    click.echo('FLASK_APP=app.py flask run')
    return True
