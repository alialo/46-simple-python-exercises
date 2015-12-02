# -*- coding: utf-8 -*- 

"""Write a function translate() that will translate a text into 
"rövarspråket" (Swedish for "robber's language"). That is, double every 
consonant and place an occurrence of "o" in between. For example, 
translate("this is fun") should return the string "tothohisos isos 
fofunon"."""

def translate(x):
  v = ['a','e','i','o','u']
  return "".join(["%so%s" % (i,i) if i not in v and i != " " else i for i in x])

print translate("this is fun")

"""Lots of fun writing this one. For reference, it's called a list 
comprehension (as far as I know not in php?)

- AoAlolanon LoLonongogsostotafoffof"""
