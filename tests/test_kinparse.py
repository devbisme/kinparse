import pytest
from kinparse import *
from .setup_teardown import *

def test_kinparse_1():
    ntlst = parse_netlist(r'C:\xesscorp\KiCad\tools\kinparse\tests\test.net')
    a = ntlst.design.source.val

def test_kinparse_2():
    ntlst = parse_netlist(r'C:\xesscorp\KiCad\tools\kinparse\tests\gardenlight.net')
    a = ntlst.design.source.val

def test_kinparse_3():
    ntlst = parse_netlist(r'C:\xesscorp\KiCad\tools\kinparse\tests\ref2by2.net')
    a = ntlst.design.source.val
