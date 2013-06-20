#!/usr/bin/env python

import os
import sys
from pyactivityextractor import extract_from_fit

out = extract_from_fit("../tests/data/unico_che_ho.FIT")
for v in out:
	print v
