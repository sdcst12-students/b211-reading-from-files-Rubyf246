#!python3
'''
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5

 
'''

def find(needle):
    datatask1 = 'task01.txt'
    data1 = open(datatask1,'r')
    data = data1.read()
    with open(datatask1) as fd:
        for n, line in enumerate(fd):
            s = line.strip()
            if s == needle:
                return n    
    return -1


if __name__ == "__main__":
     
    assert find('apple') == 0
    assert find('fish') == 5