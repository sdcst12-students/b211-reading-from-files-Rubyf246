"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

def split_list(biglist):
    list_of_lists = []
    for i in range(0, len(biglist), 4):
        list_of_3 = biglist[i:i + 3]
        #print(list_of_3)
        list_of_lists.append(list_of_3)
    return list_of_lists


def find_Pythagorean_triples(filename):
    num_of_Pythagorean_triples = 0
    #filename = 'task02a.txt'
    file = open(filename,'r')
    #print(f"This file is of type: {type(file)}" )
    data = file.read()
    #print(f"data type: {type(data)}" )
    lineData = data.split("\n")

    newList = []
    for line in lineData:
        newList.append(line)
    list_of_list_of3 =  split_list(newList)
    #print (list_of_list_of3)
    
    list_Pythagorean_triples = []
    
    for list_of3 in list_of_list_of3:
        if (list_of3[0] != ""):
            list_of3.sort()
            c = int(list_of3[2])
            a = int(list_of3[1])
            b = int(list_of3[0])
            if (c == (a**2 + b**2) ** 0.5):
                num_of_Pythagorean_triples = num_of_Pythagorean_triples + 1
                list_Pythagorean_triples.append(list_of3)
    print (list_Pythagorean_triples)            
    return  num_of_Pythagorean_triples   
    
if __name__ == "__main__":
    num_Pythagorean_triples_2a = find_Pythagorean_triples('task02a.txt') 
    num_Pythagorean_triples_2b = find_Pythagorean_triples('task02b.txt') 
    num_Pythagorean_triples_2c = find_Pythagorean_triples('task02c.txt') 
    
 
    
    dict = { '2a': num_Pythagorean_triples_2a, '2b': num_Pythagorean_triples_2b, '2c': num_Pythagorean_triples_2c }
    print (dict)