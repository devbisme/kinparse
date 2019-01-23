# MIT license
# 
# Copyright (C) 2016 by XESS Corporation.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


"""
Parsers for netlist files of various formats (only KiCad, at present).
"""


from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library
standard_library.install_aliases()

from .py_2_3 import *

from pyparsing import *


THIS_MODULE = locals()

def _parse_netlist_kicad(text):
    """
    Return a pyparsing object storing the contents of a KiCad netlist.
    """

    def _paren_clause(keyword, subclause):
        """
        Create a parser for a parenthesized list with an initial keyword.
        """
        lp = Literal('(').suppress()
        rp = Literal(')').suppress()
        kw = CaselessKeyword(keyword).suppress()
        clause = lp + kw + subclause + rp
        return clause

    #++++++++++++++++++++++++++++ Parser Definition +++++++++++++++++++++++++++

    # Basic elements.
    word = Word(alphas)
    inum = Word(nums)
    fnum = Word(nums) + Optional(Literal('.') + Optional(Word(nums)))
    string = ZeroOrMore(White()).suppress() + CharsNotIn('()') + ZeroOrMore(White()).suppress()
    qstring = dblQuotedString() ^ sglQuotedString()
    qstring.addParseAction(removeQuotes)
    anystring = qstring ^ string

    # Design section.
    source = _paren_clause('source', Optional(anystring)('val'))('source')
    date = _paren_clause('date', Optional(anystring)('val'))('date')
    tool = _paren_clause('tool', Optional(anystring)('val'))('tool')
    number = _paren_clause('number', inum('val'))('number')
    name = _paren_clause('name', anystring('val'))('name')
    names = _paren_clause('names', anystring('val'))('names')
    tstamp = _paren_clause('tstamp', anystring('val'))('tstamp')
    tstamps = _paren_clause('tstamps', anystring('val'))('tstamps')
    title = _paren_clause('title', Optional(anystring)('val'))('title')
    company = _paren_clause('company', Optional(anystring)('val'))('company')
    rev = _paren_clause('rev', Optional(anystring)('val'))('rev')
    value = _paren_clause('value', anystring('val'))('value')
    comment = _paren_clause('comment', Group(number & value))
    comments = Group(OneOrMore(comment))('comments')
    title_block = Group(_paren_clause('title_block', Optional(title) &
                        Optional(company) & Optional(rev) &
                        Optional(date) & Optional(source) & comments))('title_block')
    sheet = _paren_clause('sheet', Group(number + name + tstamps + Optional(title_block)))
    sheets = OneOrMore(sheet)('sheets')
    design = _paren_clause('design', Optional(source) & Optional(date) &
                        Optional(tool) & Optional(sheets))('design')

    # Components section.
    ref = _paren_clause('ref', anystring('val'))('ref')
    datasheet = _paren_clause('datasheet', anystring('val'))('datasheet')
    field = Group(_paren_clause('field', name & anystring('val')))
    fields = _paren_clause('fields', ZeroOrMore(field)('fields'))
    lib = _paren_clause('lib', anystring('val'))('lib')
    part = _paren_clause('part', anystring('val'))('part')
    footprint = _paren_clause('footprint', anystring('val'))('footprint')
    description = _paren_clause('description', anystring('val'))('desc')  # Gets used here and in libparts.
    libsource = _paren_clause('libsource', lib & part & Optional(description))
    sheetpath = _paren_clause('sheetpath', names & tstamps)('sheetpath')
    comp = Group(_paren_clause('comp', ref & value & Optional(datasheet) & 
                    Optional(fields) & Optional(libsource) & Optional(footprint) & 
                    Optional(sheetpath) & Optional(tstamp)))
    components = _paren_clause('components', ZeroOrMore(comp)('components'))

    # Part library section.
    docs = _paren_clause('docs', anystring('val'))('docs')
    pnum = _paren_clause('num', anystring('val'))('num')
    ptype = _paren_clause('type', anystring('val'))('type')
    pin = _paren_clause('pin', Group(pnum & name & ptype))
    pins = _paren_clause('pins', ZeroOrMore(pin))('pins')
    alias = _paren_clause('alias', anystring('val'))
    aliases = _paren_clause('aliases', ZeroOrMore(alias))('aliases')
    fp = Group(_paren_clause('fp', anystring('val')))
    footprints = _paren_clause('footprints', ZeroOrMore(fp))('footprints')
    libpart = Group(_paren_clause('libpart', lib & part & Optional(
        fields) & Optional(pins) & Optional(footprints) & Optional(aliases) &
                                  Optional(description) & Optional(docs)))
    libparts = _paren_clause('libparts', ZeroOrMore(libpart))('libparts')

    # Libraries section.
    logical = _paren_clause('logical', anystring('val'))('name')
    uri = _paren_clause('uri', anystring('val'))('uri')
    library = Group(_paren_clause('library', logical & uri))
    libraries = _paren_clause('libraries', ZeroOrMore(library))('libraries')

    # Nets section.
    #code = _paren_clause('code', inum('val'))('code')
    code = _paren_clause('code', inum('code'))
    part_pin = _paren_clause('pin', anystring('pin'))
    node = _paren_clause('node', Group(ref & part_pin))
    nodes = Group(OneOrMore(node))('nodes')
    net = _paren_clause('net', Group(code & name & nodes))
    nets = _paren_clause('nets', ZeroOrMore(net))('nets')

    # Entire netlist.
    version = _paren_clause('version', word('val'))('version')
    end_of_file = ZeroOrMore(White()) + stringEnd
    parser = _paren_clause('export', version +
                (design & components & Optional(libparts) & Optional(libraries) & nets
                )) + end_of_file.suppress()

    return parser.parseString(text)


def parse_netlist(src, tool='kicad'):
    """
    Return a pyparsing object storing the contents of a netlist.

    Args:
        src: Either a text string, or a filename, or a file object that stores
            the netlist.

    Returns:
        A pyparsing object that stores the netlist contents.

    Exception:
        PyparsingException.
    """

    try:
        text = src.read()
    except Exception:
        try:
            text = open(src,'r').read()
        except Exception:
            text = src

    if not isinstance(text, basestring):
        raise Exception("What is this shit you're handing me? [{}]\n".format(src))

    try:
        # Use the tool name to find the function for loading the library.
        func_name = '_parse_netlist_{}'.format(tool)
        parse_func = THIS_MODULE[func_name]
        return parse_func(text)
    except KeyError:
        # OK, that didn't work so well...
        logger.error('Unsupported ECAD tool library: {}'.format(tool))
        raise Exception
