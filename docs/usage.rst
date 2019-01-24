========
Usage
========

To use kinparse in a project::

    from kinparse import parse_netlist

There is a single function that will parse a KiCad EESCHEMA netlist file, a file object, or a text string
and return a `pyparsing object <https://pypi.python.org/pypi/pyparsing>`_ ::

    nlst = parse_netlist('my_schematic.net')

Then you can query the parsing object as shown below to get information about the netlist.

* Global netlist information:
    * ``nlst.version``: Netlist format version.

* Global design information:
    * ``nlst.source``: File name for the top-level schematic that generated this netlist.
    * ``nlst.date``: Date the schematic was created.
    * ``nlst.tool``: Tool used to create the schematic.

* Schematic sheet information:
    * ``nlst.sheets``: List of sheets for the schematic.
    * ``len(nlst.sheets)``: Number of sheets in the list.
    * ``nlst.sheets[0].num``: Number of the first schematic sheet.
    * ``nlst.sheets[0].name``: Name of the first schematic sheet.
    * ``nlst.sheets[0].tstamps``: Time stamp of the first schematic sheet.
    * ``nlst.sheets[0].title``: Title of the first schematic sheet.
    * ``nlst.sheets[0].company``: Name of company.
    * ``nlst.sheets[0].rev``: Revision number of the first schematic sheet.
    * ``nlst.sheets[0].date``: Date of the first schematic sheet.
    * ``nlst.sheets[0].source``: Source file for the first schematic sheet.
    * ``nlst.sheets[0].comments``: List of comments for the first schematic sheet.
    * ``len(nlst.sheets[0].comments)``: Number of comments for the first schematic sheet.
    * ``nlst.sheets[0].comments[0].num``: Number of the first comment.
    * ``nlst.sheets[0].comments[0].text``: Text of the first comment.

* Library information:
    * ``nlst.libraries``: List of libraries used in the netlist.
    * ``len(nlst.libraries)``: Number of libraries in the list.
    * ``nlst.libraries[0].name``: Name of the first library.
    * ``nlst.libraries[0].uri``: File location of the first library.

* Library of components:
    * ``nlst.libparts``: List of part types used in the netlist.
    * ``len(nlst.libparts)``: Number of part types in the list.
    * ``nlst.libparts[0].lib``: Library containing the first part.
    * ``nlst.libparts[0].name``: Part type name of the first part.
    * ``nlst.libparts[0].desc``: Description of the first part.
    * ``nlst.libparts[0].docs``: Document file name for the first part.
    * ``nlst.libparts[0].fields``: List of fields for the first part.
    * ``len(nlst.libparts[0].fields)``: Number of fields for the first part.
    * ``nlst.libparts[0].fields[0].name``: Name of the first field of the first part.
    * ``nlst.libparts[0].fields[0].value``: Value assigned to the first field of the first part.
    * ``nlst.libparts[0].pins``: List of pins for the first part.
    * ``len(nlst.libparts[0].pins)``: Number of pins on the first part.
    * ``nlst.libparts[0].pins[0].num``: Pin number of the first pin of the first part.
    * ``nlst.libparts[0].pins[0].name``: Pin name of the first pin of the first part.
    * ``nlst.libparts[0].pins[0].type``: Electrical type of the first pin of the first part.
    * ``nlst.libparts[0].footprints``: List of footprints for the first part.
    * ``len(nlst.libparts[0].footprints)``: Number of footprints for the first part.
    * ``nlst.libparts[0].footprints[0]``: First footprint for the first part.
    * ``nlst.libparts[0].aliases``: List of aliases for the first part.
    * ``len(nlst.libparts[0].aliases)``: List of aliases for the first part.
    * ``nlst.libparts[0].aliases[0]``: First alias for the first part.

* parts:
    * ``nlst.parts``: List of part instances used in the netlist.
    * ``len(nlst.parts)``: Number of parts used in the list.
    * ``nlst.parts[0].ref``: Reference designator for the first part.
    * ``nlst.parts[0].value``: Value of the first part.
    * ``nlst.parts[0].tstamp``: Time stamp for the first part.
    * ``nlst.parts[0].datasheet``: File location of datasheet for the first part.
    * ``nlst.parts[0].lib``: Name of the library containing the first part.
    * ``nlst.parts[0].name``: Part type name for the first part.
    * ``nlst.parts[0].desc``: Description for the first part.
    * ``nlst.parts[0].footprint``: PCB footprint for the first part.
    * ``nlst.parts[0].sheetpath.names``: Sheet name on which the first part appears.
    * ``nlst.parts[0].sheetpath.tstamps``: Time stamp for the sheet on which the first part appears.
    * ``nlst.parts[0].fields``: List of fields for the first part.
    * ``len(nlst.parts[0].fields)``: Number of fields for the first part.
    * ``nlst.parts[0].fields[0].name``: Name of the first field of the first part.
    * ``nlst.parts[0].fields[0].value``: Value assigned to the first field of the first part.

* Net connections:
    * ``nlst.nets``: List of nets connecting the component pins.
    * ``len(nlst.nets)``: Number of nets in the list.
    * ``nlst.nets[0].name``: Name of the first net.
    * ``nlst.nets[0].code``: Code number for the first net.
    * ``nlst.nets[0].pins``: List of pins attached to the first net.
    * ``len(nlst.nets[0].pins)``: Number of pins attached to the first net.
    * ``nlst.nets[0].pins[0].ref``: Part reference designator for first pin on the first net.
    * ``nlst.nets[0].pins[0].num``: Pin number of referenced part for the first pin on the first net.
