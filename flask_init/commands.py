import os
import click
from jinja2 import Environment, PackageLoader

single_module_path = 'templates/single_module'
package_path = 'templates/package'
blueprints_path = 'templates/blueprints'


@click.command()
@click.option('--single-module', is_flag=True)
@click.option('--package', is_flag=True)
@click.option('--blueprints', is_flag=True)
def cli(single_module, package, blueprints):
    """
    Easy way to create Flask Web application.
    """
    click.echo(single_module)
    click.echo(package)
    click.echo(blueprints)
    if single_module:
        # import pdb; pdb.set_trace()
        for root, dirs, files in os.walk(single_module_path):
            for name in dirs:
                click.echo(os.path.join(root, name))

            for name in files:
                click.echo(os.path.join(root, name))

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
