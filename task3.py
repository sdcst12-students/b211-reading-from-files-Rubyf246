#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

def sum():
    list_sum = []
    sum = 0
    datatask1 = 'task03.txt'
    data1 = open(datatask1,'r')
    data = data1.read()

    myarray = data.split("\n\n")
    for line in myarray:
        sum = 0
        myarray2 = line.split("\n")
        for line2 in myarray2:
            
            #print(line2.strip("\n"))
            if (line2.strip("\n") != ""):
                sum = sum + int(line2.strip("\n"))  
        
        list_sum.append(sum)
        #print(list_sum)
        
    return max(list_sum)   
        
if __name__ == "__main__":        
    print("the largest sum is: " + str(sum()))