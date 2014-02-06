#!/usr/bin/python
 
# -*- coding: utf-8 -*-

# Copyright (c) 2014, Alexander O'Connor 
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


""" convert csv to json """

import os 
import sys
import csv
import json 
import re # now I have 2 problems :)
import argparse

#Takes data from MFP and produces a CSV
#Get the data from the reports button using the chrome inspector tools

__author__ = "Alexander O'Connor <oconnoat@gmail.com>"
__copyright__ = "Copyright 2014, Alexander O'Connor <oconnoat@gmail.com>"
__credits__ = ["Alexander O'Connor <oconnoat@gmail.com>"]
__license__ = "BSD, 3-line"
__version__ = "0.1"
__email__ = "Alexander O'Connor <oconnoat@gmail.com>"
__status__ = "Prototype"

def json_to_csv(jsonfile, filename):
    #read in the json and make a dict
    data = json.load(open(jsonfile))
    
    with open(filename,'wb') as csvfile:
        writer = csv.writer(csvfile)
        for values in data['data']:
            date_pat = re.compile(r'(\d)/(\d\d)')
            #TODO: Handle years, right now needs manual editing.
            #converts from mm/dd to MM-DD-20XX 
            writer.writerow([date_pat.sub(r'\1-\2-20XX', str(values['date'])),values['total']])

if __name__ == "__main__":    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--infile", help="filepath for the JSON to read.", required=True)
    parser.add_argument("-o","--outfile", help="filepath for the CSV to write.", required=True)
    args = parser.parse_args()
    json_to_csv(args.infile, args.outfile) 
