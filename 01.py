#!/usr/bin/python

from pprint import pprint
import traceback
import pickle

data = {'A': [1,'kl'], 'B': [1]}
try:
  data['C'] = 2
except KeyError, e:
  traceback.print_exc()

pprint(data)  
#! a datastructure from the collections module allows the append operation
#d_data = ???
#d_data.update(data)
#d_data['C'].append(2)
#pprint(d_data)

