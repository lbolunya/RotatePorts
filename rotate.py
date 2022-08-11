# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 22:11:36 2022

Title: rotate.py
Purpose: Convert port numbering of S4P touchstone file.
Author: luis.boluna@keysight.com
Known issues/limitations:
    Expand use of ports 
     - Check port numbering for errors
     - Not hard code ports, for other applications
    
    Examples:
    
python rotate.py filename.s4p
python rotate.py filename.s4p --newfile foo.s4p
"""

import skrf as rf
import os
from typing import Sequence

def rotate_ports(FILENAME, NEWFILENAME):
    try:
        s4p_in = rf.Network(FILENAME)
    except:
        raise ValueError('File: '+FILENAME+' does not exist')
    nports = s4p_in.nports
    if nports != 4:
        raise ValueError('Number of ports is not 4 but '+nports)
    s4p_in.renumber([0,1,2,3],[0,2,1,3])
    print("\n>>> Port 1 unchanged to Port 1")
    print(">>> Port 2 swapped to Port 3")
    print(">>> Port 3 swapped to Port 2")
    print(">>> Port 4 unchanged to Port 4")
    file, file_extension = os.path.split(NEWFILENAME)
    
    if file_extension !=  's4p':
        s4p_in.write_touchstone(NEWFILENAME+'.s4p')
        print("\n File saved: {}\n".format(NEWFILENAME+'.s4p'))
    else:
        s4p_in.write_touchstone(NEWFILENAME)
        print("\n File saved: {}\n".format(NEWFILENAME))

#def parse_ports(port_in):
#    return [0,1,2,3],[0,2,1,3]


def main():
    import argparse
    
    help_header = "\n\n" \
                  "================================================\n" \
                  "Converts port numbering of S4P touchstone file.\n"\
                  "\n" \
                  "Example:\n\n" \
                  "python rotate.py filename.s4p\n"\
                  "\n" \
                  "or,\n" \
                  "\n" \
                  "python rotate.py filename.s4p --newfile foo.s4p\n" \
                  "\n\n" \
                  "Version 1.0    ---    luis.boluna@keysight.com\n"\
                  "================================================\n\n"

    parser = argparse.ArgumentParser(help_header)
    parser.add_argument('file', metavar = 'file', type=str, help = "The filename of the touchstone S4P file")
    parser.add_argument('--newfile', type=str, required=False, help = "New filename if it is not same as original")
    #parser.add_argument('--ports', type=str, required=False, help = "example: [1,2,3,4],[1,3,2,4]")
    args = parser.parse_args()
    
    # if args.ports:
    #     port = parse_ports(args.ports)
    # else:
    #     port = "[0,1,2,3],[0,2,1,3]"
    
    if args.newfile:
        rotate_ports(args.file, args.newfile)
    else:
        rotate_ports(args.file. args.file) 
    
if __name__ == "__main__":
        main()
