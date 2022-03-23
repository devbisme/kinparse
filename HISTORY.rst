.. :changelog:

History
-------


1.1.0 (2022-03-23)
______________________

* Updated to handle both KiCad V5 and V6 netlist files.


1.0.0 (2021-09-17)
______________________

* Decided this tool was mature enough that it could be called 1.0.0.


0.1.2 (2019-02-23)
______________________

* Files are now opened with latin_1 encoding to allow special symbols used by KiCad.


0.1.1 (2019-01-28)
______________________

* Fixed problem where sheetpath.names and sheetpath.tstamps were not retrievable.


0.1.0 (2019-01-24)
______________________

* Restructured the parser to make it work with the current version of pyparsing.


0.0.5 (2018-12-30)
______________________

* Restricted pyparsing package to version < 2.3.0 because that one started breaking things.


0.0.4 (2018-08-27)
______________________

* KiCad V5 started putting description fields in component libsource.


0.0.3 (2018-02-14)
______________________

* Non-numeric revision is now allowed in the netlist rev field.


0.0.2 (2017-12-21)
______________________

* Fixed parse errors caused by fields with labels but no data like "(date)" .


0.0.1 (2017-07-12)
______________________

* First release on PyPI.
