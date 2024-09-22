# -*- coding: utf-8 -*-

from skidl import *


def _home_devb_tech_stuff_KiCad_tools_kinparse_tests_data_kicad6_test_2_kicad_sch():

    #===============================================================================
    # Component templates.
    #===============================================================================

    Device_Q_NPN_CBE = Part('Device', 'Q_NPN_CBE', dest=TEMPLATE)

    Device_R_US = Part('Device', 'R_US', dest=TEMPLATE)


    #===============================================================================
    # Component instantiations.
    #===============================================================================

    Q1 = Device_Q_NPN_CBE(ref='Q1', value='Q_NPN_CBE')

    R1 = Device_R_US(ref='R1', value='R_US')

    R2 = Device_R_US(ref='R2', value='R_US')

    R3 = Device_R_US(ref='R3', value='R_US')

    R4 = Device_R_US(ref='R4', value='R_US')

    R5 = Device_R_US(ref='R5', value='R_US')


    #===============================================================================
    # Net interconnections between instantiated components.
    #===============================================================================

    Net('+5V').connect(R2['1'], R4['1'])

    Net('GND').connect(R3['2'], R5['2'])

    Net('IN').connect(R1['1'])

    Net('Net-(R1-Pad2)').connect(Q1['2'], R1['2'], R2['2'], R3['1'])

    Net('Net-(R5-Pad1)').connect(Q1['3'], R5['1'])

    Net('OUT').connect(Q1['1'], R4['2'])


#===============================================================================
# Instantiate the circuit and generate the netlist.
#===============================================================================

if __name__ == "__main__":
    _home_devb_tech_stuff_KiCad_tools_kinparse_tests_data_kicad6_test_2_kicad_sch()
    generate_netlist()
