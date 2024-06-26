# Introduction
Sequences are one of the principal built-in data types besides numerics, mappings, files, instances and exceptions. Python provides for six sequential data types. 

* Strings
* Byte arrays
* Byte sequences
* Lists
* Tuples
* Range objects

Strings, lists, tuples, bytes and range objects might look different, but they have some concepts in common. 
The items or elements of strings, lists and tuples are ordered in a defined sequence. The elements can be accessed via indices. Python uses the same syntax and function names to work on sequential data types. For example, length of a string, a list and a tuple can be found with a function called len(). 

# Bytes

The byte object is a sequence of small integers. The elements of a byte object are in the range 0 to 255, corresponding to ASCII characters. 

I am going to talk about rest of the topics in Sequential data types in separate files. 
Information about Python Lists is mentioned [here](./lists.py)

# Tuples

A tuple is an immutable list i.e. a tuple cannot be changed in any way, once it has been created.

Benefits? 
* Tuples are faster than lists. 
* When to use -> If you know your data doesn't have to be changed, you should use tuple as this protects your data against accidental changes. 
* Tuples can also be used as keys in dictionaries, while lists can't. 