import pytest
from kinparse import *
from .setup_teardown import *

def isstr(s):
    print(s)
    assert isinstance(s, (type(u"A"), type("A"), type("")))

def parser_tests(ntlst):
    isstr(ntlst.version)

    isstr(ntlst.source)
    isstr(ntlst.date)
    isstr(ntlst.tool)
    isstr(ntlst.sheets[0].num)
    isstr(ntlst.sheets[0].name)
    isstr(ntlst.sheets[0].tstamps)
    isstr(ntlst.sheets[0].title)
    isstr(ntlst.sheets[0].company)
    isstr(ntlst.sheets[0].rev)
    isstr(ntlst.sheets[0].date)
    isstr(ntlst.sheets[0].source)
    isstr(ntlst.sheets[0].comments[0].num)
    isstr(ntlst.sheets[0].comments[0].text)

    isstr(ntlst.libraries[0].name)
    isstr(ntlst.libraries[0].uri)

    isstr(ntlst.libparts[0].lib)
    isstr(ntlst.libparts[0].name)
    isstr(ntlst.libparts[0].desc)
    isstr(ntlst.libparts[0].docs)
    isstr(ntlst.libparts[0].fields[0].name)
    isstr(ntlst.libparts[0].fields[0].value)
    isstr(ntlst.libparts[0].pins[0].num)
    isstr(ntlst.libparts[0].pins[0].name)
    isstr(ntlst.libparts[0].pins[0].type)
    if len(ntlst.libparts[0].footprints):
        isstr(ntlst.libparts[0].footprints[0])
    if len(ntlst.libparts[0].aliases):
        isstr(ntlst.libparts[0].aliases[0])

    isstr(ntlst.parts[0].ref)
    isstr(ntlst.parts[0].value)
    isstr(ntlst.parts[0].tstamp)
    isstr(ntlst.parts[0].datasheet)
    isstr(ntlst.parts[0].lib)
    isstr(ntlst.parts[0].part)
    isstr(ntlst.parts[0].desc)
    isstr(ntlst.parts[0].footprint)
    isstr(ntlst.parts[0].sheetpath.names)
    isstr(ntlst.parts[0].sheetpath.tstamps)
    if len(ntlst.parts[0].fields):
        isstr(ntlst.parts[0].fields[0].name)
        isstr(ntlst.parts[0].fields[0].value)

    isstr(ntlst.nets[0].name)
    isstr(ntlst.nets[0].code)
    isstr(ntlst.nets[0].pins[0].ref)
    isstr(ntlst.nets[0].pins[0].num)


def test_kinparse_1():
    ntlst = parse_netlist('data/test.net')
    assert len(ntlst.nets) == 30
    parser_tests(ntlst)

def test_kinparse_2():
    ntlst = parse_netlist('data/gardenlight.net')
    assert len(ntlst.nets) == 34
    parser_tests(ntlst)

def test_kinparse_3():
    ntlst = parse_netlist('data/ref2by2.net')
    assert len(ntlst.nets) == 4
    parser_tests(ntlst)

def test_kinparse_4():
    ntlst = parse_netlist('data/gaillard.net')
    assert ntlst.parts[0].sheetpath.names == "/Logic/"
    assert ntlst.parts[0].sheetpath.tstamps == "/5C4D0F9E/"
    assert ntlst.parts[0].tstamp == "5C4D541F"
    parser_tests(ntlst)

def test_kinparse_5():
    ntlst = parse_netlist('data/kicad5_test.net')
    assert len(ntlst.parts) == 6
    assert len(ntlst.nets) == 6
    parser_tests(ntlst)

def test_kinparse_6():
    ntlst = parse_netlist('data/kicad6_test.net')
    assert len(ntlst.parts) == 6
    assert len(ntlst.nets) == 6
    parser_tests(ntlst)
