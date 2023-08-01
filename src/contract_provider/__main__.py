"""Perform starting configurations for the contract consumer."""
from . import project


def entry_point():
    """Entry point function that sets up the contract consumer project."""
    version = project.Project.get_version()
    print(f"Project version: {version}")  # TODO: replace with logging


entry_point()
