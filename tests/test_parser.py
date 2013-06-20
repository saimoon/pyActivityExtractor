#!/usr/bin/env python

import os
import sys

from pyactivityextractor import extract_from_fit

from StringIO import StringIO
import datetime
import unittest


FILENAME = os.path.join(os.path.dirname(__file__), 'data', "unico_che_ho.FIT")
DATA = open(FILENAME, 'rb').read()


class FitFileTestCase(unittest.TestCase):
    maxDiff = None
    def test_fitfile_extractor(self):
        out = extract_from_fit(StringIO(DATA))

        resulting_dictionary = {
                                'sub_sport': {'units': None, 'data': 'generic'}, 
                                'total_calories': {'units': 'kcal', 'data': 159}, 
                                'total_timer_time': {'units': 's', 'data': 2007.162}, 
                                'timestamp': {'units': 's', 'data': datetime.datetime(2013, 6, 6, 12, 1, 50)}, 
                                'start_time': {'units': None, 'data': datetime.datetime(2013, 6, 6, 11, 28, 15)}, 
                                'total_elapsed_time': {'units': 's', 'data': 2007.162}, 
                                'start_position_lat': {'units': 'semicircles', 'data': 620185595}, 
                                'total_distance': {'units': 'm', 'data': 2880.21}, 
                                'avg_speed': {'units': 'm/s', 'data': 1.435}, 
                                'sport': {'units': None, 'data': 'running'}, 
                                'start_position_long': {'units': 'semicircles', 'data': 70523281}
                               }

        self.assertDictEqual(out[0], resulting_dictionary)


if __name__ == '__main__':
    unittest.main()
