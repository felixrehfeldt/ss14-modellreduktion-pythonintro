#!/usr/bin/python

def foo(bar = []):
    if bar != []:
        bar.append('o')
        return bar
    else:
        return ['o']


#! fix the function so all calls return the same
print(foo())
print(foo())
print(foo())
print(foo([]))