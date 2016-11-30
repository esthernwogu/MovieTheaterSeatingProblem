# -*- coding: utf-8 -*-
#!/usr/bin/env python

from lib import Theater

import argparse 
import os.path

def filecheck(filepath):
    """
    Checks if file exists
    """
    if not os.path.exists(filepath):
        #argparse gives error message with ArgumentTypeError
        raise argparse.ArgumentTypeError("{0} does not exist".format(filepath))
    return filepath

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MovieReservations")
    parser.add_argument(dest = "filename",help = "input file with reservations")
    args = parser.parse_args() 
    
    print(args.filename)
    movieTheater = Theater.Theater(10,20, args.filename)
    movieTheater.Assign()
    movieTheater.WriteOutputToFile()
    #movieTheater.DisplayAssignmentResult()