import pytest
from kinparse import *
from .setup_teardown import *

def test_kinparse_1():
    ntlst = parse_netlist('tests/data/test.net')
    assert len(ntlst) == 69
    a = ntlst.design.source.val

def test_kinparse_2():
    ntlst = parse_netlist('tests/data/gardenlight.net')
    assert len(ntlst) == 93
    a = ntlst.design.source.val

def test_kinparse_3():
    ntlst = parse_netlist('tests/data/ref2by2.net')
    assert len(ntlst) == 13
    a = ntlst.design.source.val
