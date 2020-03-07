# traveling salesman problem
# ant colonization
import sys
import math

class City(object):
    def __init__(self,key,point):
        self.key = key # city number
        self.point = point #(x,y), where x is index 0 and y is index 1



class Graph(object):
    def __init__(self):
        pass

def main():
    pass

print("Argument List:", str(sys.argv))
text_name = str(sys.argv[1])


file = open(text_name, "r")
lines = file.readlines() # reads all the lines in the file
file.close()
current_line = 0

int_string = []
for num in range(len(lines)):
    int_string.append([int(i) for i in lines[num].split() if i.isdigit()])
print (int_string)


cities = []
for i in range(len(int_string)):
    cities.append(City(int_string[i][0],int_string[i][1:]))











def distance(c1,c2):
    #x=[0] y=[1]
    x = c1[0] - c2[0]
    y = c1[1] - c2[1]
    total = math.sqrt(x**2 + y**2)
    return round(total)
