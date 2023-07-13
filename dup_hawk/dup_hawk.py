import click
from __version__ import __title__, __version__


@click.command()
@click.version_option(
    version=__version__,
    prog_name=__title__,
)
def mark_duplicates_click():
    pass


def mark_duplicates():
    pass


if __name__ == "__main__":
    mark_duplicates_click()
