"""Hello World unit tests."""
import pytest

from helloworld.helloworld import HelloWorld

@pytest.mark.skip("for demo")
@pytest.mark.parametrize(
    "name",
    [
        "Zeno Zolydck",
        "Issac Netero",
        "Meruem",
        "Chrollo Lucilfer",
        "Hisoka Morow",
    ],
)
def test_get_message(name):
    """Check the gretting message.

    Parameters
    ----------
    name : str
        Name of the entity to be greeted.

    """
    helloworld = HelloWorld()
    assert helloworld.get_message(name) == f"Hello {name}!"
