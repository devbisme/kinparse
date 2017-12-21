import pytest
from kinparse import *
from .setup_teardown import *

def test_kinparse_1():
    parse_netlist(r'C:\xesscorp\KiCad\tools\kinparse\tests\test.net')

def test_kinparse_2():
    parse_netlist(r'C:\xesscorp\KiCad\tools\kinparse\tests\gardenlight.net')
