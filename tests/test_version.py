import mmflyer
from mmflyer import __version__


def test_version():
    """Return current application version string"""
    mmf = mmflyer
    assert mmf.version() == __version__
