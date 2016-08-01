from context import utilities
from utilities import paramiko_sftp as ps

def test_readauth():
    assert len(ps.read_auth()) == 4
