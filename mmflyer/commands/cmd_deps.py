from mmflyer import __version__
from stl import __about__
import click

@click.command("deps", help="Display dependency versions.")
def cli():
    """Display current dependency versions."""
    osc = OpenSCAD()
    osc_version = osc.get_version()
    click.echo(f"mmf: {__version__}")
    click.echo(f"numpy-stl: {__about__.__version__}")