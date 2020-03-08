# traveling salesman problem
# ant colonization
import sys
import math

class Tour(object):
    def __init__(self):
        pass


class City(object):
    def __init__(self,city_num,point):
        self.city_num = city_num # city number
        self.point = point #(x,y), where x is index 0 and y is index 1


class Graph(object):
    def __init__(self):
        self.edge = edge
        self.c1 = c1
        self.c2 = c2
        self.distance = distance

def main():
    pass

print("Argument List:", str(sys.argv))
text_name = str(sys.argv[1])

# reading the files
file = open(text_name, "r")
lines = file.readlines() # reads all the lines in the file
file.close()
current_line = 0

int_string = []
for num in range(len(lines)):
    int_string.append([int(i) for i in lines[num].split() if i.isdigit()])
print (int_string)

# list of points
cities = []
for i in range(len(int_string)):
    cities.append(City(int_string[i][0],int_string[i][1:]))
    print("key = %s  coordinate: %s "% (cities[i].city_num, cities[i].point))

adj_matrix = [[0 for i in range(len(lines))] for j in range(len(lines))]









def distance(c1,c2):
    #x=[0] y=[1]
    x = c1[0] - c2[0]
    y = c1[1] - c2[1]
    total = math.sqrt(x**2 + y**2)
    return round(total)



main()
