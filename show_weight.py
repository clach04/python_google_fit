#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#
"""Process Google Fit Takeout CSV summary file and show weight information
"""

import csv
import os
import sys


def doit(filename):
    """
    reader = csv.reader(open(filename))
    data = []
    for row in reader:
        data.append(row)
    print(data)
    """
    has_header = True
    reader = csv.reader(open(filename))
    if has_header:
        header = reader.next()
    if header != ['Date', 'Calories (kcal)', 'Distance (m)', 'Average speed (m/s)', 'Max speed (m/s)', 'Min speed (m/s)', 'Step count', 'Average weight (kg)', 'Max weight (kg)', 'Min weight (kg)', 'Biking duration (ms)', 'Walking duration (ms)', 'Running duration (ms)', 'Spinning duration (ms)', 'Kickboxing duration (ms)', 'Sleep duration (ms)', 'Deep sleeping duration (ms)']:  # as of April 2019
        print('WARNING header different than expected')
        print(header)
    AVERAGE_WEIGHT, MAX_WEIGHT, MIN_WEIGHT = ('Average weight (kg)', 'Max weight (kg)', 'Min weight (kg)')
    for row in reader:
        record = dict(zip(header, row))
        average_weight = record[AVERAGE_WEIGHT]
        if average_weight:
            #print(record['Date'], average_weight)
            print('%s\t%s' % (record['Date'], average_weight))

def main(argv=None):
    if argv is None:
        argv = sys.argv

    print('Python %s on %s' % (sys.version, sys.platform))


    try:
        filename = argv[1]
    except IndexError:
        filename = 'Daily Summaries.csv'  # in directory: Takeout/Fit/Daily Aggregations
    doit(filename)

    return 0


if __name__ == "__main__":
    sys.exit(main())

