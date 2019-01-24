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
    * ``nlst.design.source``: File name for the top-level schematic that generated this netlist.
    * ``nlst.design.date``: Date the schematic was created.
    * ``nlst.design.tool``: Tool used to create the schematic.

* Schematic sheet information:
    * ``nlst.design.sheets``: List of sheets for the schematic.
    * ``len(nlst.design.sheets)``: Number of sheets in the list.
    * ``nlst.design.sheets[0].num``: Number of the first schematic sheet.
    * ``nlst.design.sheets[0].name``: Name of the first schematic sheet.
    * ``nlst.design.sheets[0].tstamps``: Time stamp of the first schematic sheet.
    * ``nlst.design.sheets[0].title``: Title of the first schematic sheet.
    * ``nlst.design.sheets[0].company``: Name of company.
    * ``nlst.design.sheets[0].rev``: Revision number of the first schematic sheet.
    * ``nlst.design.sheets[0].date``: Date of the first schematic sheet.
    * ``nlst.design.sheets[0].source``: Source file for the first schematic sheet.
    * ``nlst.design.sheets[0].comments``: List of comments for the first schematic sheet.
    * ``len(nlst.design.sheets[0].comments)``: Number of comments for the first schematic sheet.
    * ``nlst.design.sheets[0].comments[0].num``: Number of the first comment.
    * ``nlst.design.sheets[0].comments[0].text``: Text of the first comment.

* Library information:
    * ``nlst.libraries``: List of libraries used in the netlist.
    * ``len(nlst.libraries)``: Number of libraries in the list.
    * ``nlst.libraries[0].name``: Name of the first library.
    * ``nlst.libraries[0].uri``: File location of the first library.

* Library of components:
    * ``nlst.libparts``: List of component (or part) descriptions used in the netlist.
    * ``len(nlst.libparts)``: Number of component descriptions in the list.
    * ``nlst.libparts[0].lib``: Library containing the first component.
    * ``nlst.libparts[0].name``: Part name of the first component.
    * ``nlst.libparts[0].desc``: Description of the first component.
    * ``nlst.libparts[0].docs``: Document file name for the first component.
    * ``nlst.libparts[0].fields``: List of fields for the first component.
    * ``len(nlst.libparts[0].fields)``: Number of fields for the first component.
    * ``nlst.libparts[0].fields[0].name``: Name of the first field of the first component.
    * ``nlst.libparts[0].fields[0].value``: Value assigned to the first field of the first component.
    * ``nlst.libparts[0].pins``: List of pins for the first component.
    * ``len(nlst.libparts[0].pins)``: Number of pins on the first component.
    * ``nlst.libparts[0].pins[0].num``: Pin number of the first pin of the first component.
    * ``nlst.libparts[0].pins[0].name``: Pin name of the first pin of the first component.
    * ``nlst.libparts[0].pins[0].type``: Electrical type of the first pin of the first component.
    * ``nlst.libparts[0].footprints``: List of footprints for the first component.
    * ``len(nlst.libparts[0].footprints)``: Number of footprints for the first component.
    * ``nlst.libparts[0].footprints[0]``: First footprint for the first component.
    * ``nlst.libparts[0].aliases``: List of aliases for the first component.
    * ``len(nlst.libparts[0].aliases)``: List of aliases for the first component.
    * ``nlst.libparts[0].aliases[0]``: First alias for the first component.

* Components:
    * ``nlst.parts``: List of components (or parts) used in the netlist.
    * ``len(nlst.parts)``: Number of components used in the list.
    * ``nlst.parts[0].ref``: Reference designator for the first component.
    * ``nlst.parts[0].value``: Value of the first component.
    * ``nlst.parts[0].tstamp``: Time stamp for the first component.
    * ``nlst.parts[0].datasheet``: File location of datasheet for the first component.
    * ``nlst.parts[0].lib``: Name of the library containing the first component.
    * ``nlst.parts[0].name``: Part name for the first component.
    * ``nlst.parts[0].desc``: Description for the first component.
    * ``nlst.parts[0].footprint``: PCB footprint for the first component.
    * ``nlst.parts[0].sheetpath.names``: Sheet name on which the first component appears.
    * ``nlst.parts[0].sheetpath.tstamps``: Time stamp for the sheet on which the first component appears.
    * ``nlst.parts[0].fields``: List of fields for the first component.
    * ``len(nlst.parts[0].fields)``: Number of fields for the first component.
    * ``nlst.parts[0].fields[0].name``: Name of the first field of the first component.
    * ``nlst.parts[0].fields[0].value``: Value assigned to the first field of the first component.

* Net connections:
    * ``nlst.nets``: List of nets connecting the component pins.
    * ``len(nlst.nets)``: Number of nets in the list.
    * ``nlst.nets[0].name``: Name of the first net.
    * ``nlst.nets[0].code``: Code number for the first net.
    * ``nlst.nets[0].pins``: List of pins attached to the first net.
    * ``len(nlst.nets[0].pins)``: Number of pins attached to the first net.
    * ``nlst.nets[0].pins[0].ref``: Part reference designator for first pin on the first net.
    * ``nlst.nets[0].pins[0].num``: Pin number of referenced part for the first pin on the first net.
