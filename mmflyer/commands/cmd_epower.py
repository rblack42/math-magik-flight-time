import os
import click
from mmflyer.Erbach import Erbach
from mmflyer.cli import pass_environment


@click.command("epower", help="Erbach power calculator")
@pass_environment
def cli(ctx):
    """Display current dependency versions."""
    click.echo(f"generating power data")
    eb = Erbach()
    fn = os.path.join(ctx.model_path, ctx.model_name) + '.yml'
    eb.load_model_data(fn)
    print(eb.load_model())
    click.echo("Generating model power data")
