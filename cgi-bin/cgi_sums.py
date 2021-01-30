#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()
print("Your job is to make this work")

form = cgi.FieldStorage()
listval = [int(x) for x in form.getlist('operand')]

print(f"sum({listval}) = ",sum(listval))