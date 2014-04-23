#!/usr/bin/python

import time

def report_letter(c):
  print(chr(ord('z') - c))

count = 10
#! results in a en endless loop. why?
#! Antwort: weil es diesen Operator in Python nicht gibt.
while count > 0:
  count -= 1
  report_letter(count)