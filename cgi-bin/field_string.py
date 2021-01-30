#!/usr/env/bin python
import cgi

print("Content-Type: text/plain")
print("")

form = cgi.FieldStorage()
stringval = form.getvalue('a', None)
listval = form.getlist('b')

print("a",type(stringval),stringval)
print("b",type(listval),listval)