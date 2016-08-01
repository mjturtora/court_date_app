from context import utilities
from utilities import paramiko_sftp as ps


def test_ptdummy_t():
    assert ps.pt_dummy(2) == 3

def test_ptdummy_f():
    assert ps.pt_dummy(2) == 4

def test_readauth():
    assert len(ps.read_auth()) == 4

