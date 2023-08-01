"""Hello World module for the initial project setup."""


class HelloWorld:
    """Used for the initial setup of the project and supporting tools."""

    def __init__(self) -> None:
        """Initialize the module's data."""
        self.greeting = "Hello"

    def get_message(self, name):
        """Return the greeting message.

        Parameters
        ----------
        name : str
            Name of the entity to be greeted.

        Returns
        -------
        message : str
            Message to greet the named entity.

        """
        return f"{self.greeting} {name}!"
