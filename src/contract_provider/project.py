"""Information about this project for use within the project."""

import pyproject_parser


class Project:
    """Provides access to the project information from the project configuration."""

    @classmethod
    def get_version(cls):
        """Get the current project version.

        Returns
        -------
        version : str
            The current project version.

        Notes
        -----
        The project uses [semantic release](https://python-semantic-release.readthedocs.io/)
        to automatically update the project version.

        """
        if cls.__version == "":
            pyproject = pyproject_parser.PyProject().load("pyproject.toml")
            cls.__version = pyproject.tool["semantic_release"]["version"]

        return cls.__version

    __version = ""
