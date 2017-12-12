# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:40:31 2017

@author: bjr21
"""

from sas7bdat import SAS7BDAT
import os
import pandas as pd

mydir = os.getcwd()

sasfile = SAS7BDAT(os.path.join(mydir, 'grf16_lea_blkgrp.sas7bdat'))

df = sasfile.to_data_frame()

df.to_csv(os.path.join(mydir, 'BlockInfo.csv'))
