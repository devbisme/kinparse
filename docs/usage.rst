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
    * ``nlst.version.val``: Netlist format version.

* Global design information:
    * ``nlst.design.source.val``: File name for the schematic that generated this netlist.
    * ``nlst.design.date.val``: Date the schematic was created.
    * ``nlst.design.tool.val``: Tool used to create the schematic.

* Schematic sheet information:
    * ``nlst.design.sheets``: List of sheets for the schematic.
    * ``nlst.design.sheets[0].number.val``: Number of the first schematic sheet.
    * ``nlst.design.sheets[0].name.val``: Name of the first schematic sheet.
    * ``nlst.design.sheets[0].tstamps.val``: Time stamp of the first schematic sheet.
    * ``nlst.design.sheets[0].title_block.title.val``: Title of the first schematic sheet.
    * ``nlst.design.sheets[0].title_block.company.val``: Name of company.
    * ``nlst.design.sheets[0].title_block.rev.val``: Design revision number.
    * ``nlst.design.sheets[0].title_block.date.val``: Design date.
    * ``nlst.design.sheets[0].title_block.source.val``: Design source file.
    * ``nlst.design.sheets[0].title_block.comments``: List of comments.
    * ``nlst.design.sheets[0].title_block.comments[0].number.val``: Number of the first comment.
    * ``nlst.design.sheets[0].title_block.comments[0].value.val``: Text of the first comment.

* Library information:
    * ``nlst.libraries``: List of libraries used in the netlist.
    * ``nlst.libraries[0].logical.val``: Logical name of first library.
    * ``nlst.libraries[0].uri.val``: File name and location of first library.

* Components:
    * ``nlst.components``: List of components (or parts).
    * ``nlst.components[0].ref.val``: Reference for the first component.
    * ``nlst.components[0].value.val``: Value of the first component.
    * ``nlst.components[0].tstamp.val``: Time stamp for the first component.
    * ``nlst.components[0].datasheet.val``: Location of datasheet for the first component.
    * ``nlst.components[0].fields``: List of fields for the first component.
    * ``nlst.components[0].fields[0].name.val``: Name of first field of the first component.
    * ``nlst.components[0].fields[0].text``: Value assigned to first field of the first component.
    * ``nlst.components[0].libsource.lib.val``: Library containing the first component.
    * ``nlst.components[0].libsource.part.val``: Part name for the first component.
    * ``nlst.components[0].libsource.description.val``: Description for the first component.
    * ``nlst.components[0].footprint.val``: PCB footprint for the first component.
    * ``nlst.components[0].sheetpath.names.val``: Sheet name on which the first component appears.
    * ``nlst.components[0].sheetpath.tstamps.val``: Time stamp for the sheet on which the first component appears.

* Library descriptions of components:
    * ``nlst.libparts``: List of part (or component) descriptions.
    * ``nlst.libparts[0].lib.val``: Library containing the first component.
    * ``nlst.libparts[0].part.val``: Part number of the first component.
    * ``nlst.libparts[0].description.val``: Description of the first component.
    * ``nlst.libparts[0].docs.val``: Document file name for the first component.
    * ``nlst.libparts[0].fields``: List of fields for the first component.
    * ``nlst.libparts[0].fields[0].name.val``: Name of the first field of the first component.
    * ``nlst.libparts[0].fields[0].text``: Value assigned to the first field of the first component.
    * ``nlst.libparts[0].pins``: List of pins for the first component.
    * ``nlst.libparts[0].pins[0].num.val``: Pin number of the first pin of the first component.
    * ``nlst.libparts[0].pins[0].name.val``: Pin name of the first pin of the first component.
    * ``nlst.libparts[0].pins[0].type.val``: Pin type of the first pin of the first component.
    * ``nlst.libparts[0].footprints``: List of footprints for the first component.
    * ``nlst.libparts[0].footprints[0].fp.val``: First footprint for the first component.
    * ``nlst.libparts[0].aliases``: List of aliases for the first component.
    * ``nlst.libparts[0].aliases[0].text``: First alias for the first component.

* Net connections:
    * ``nlst.nets``: List of nets.
    * ``nlst.nets[0].name.val``: Name of the first net.
    * ``nlst.nets[0].code.val``: Code number for the first net.
    * ``nlst.nets[0].nodes``: List of nodes attached to the first net.
    * ``nlst.nets[0].nodes[0].ref.val``: Part reference for first node on the net.
    * ``nlst.nets[0].nodes[0].pin.val``: Pin number of part for the first node on the net.
