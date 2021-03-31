import pytest
from royalnet_console.pda import ConsolePDA


def test_construction():
    pda = ConsolePDA()
    assert pda is not None


@pytest.fixture
def pda():
    return ConsolePDA()
