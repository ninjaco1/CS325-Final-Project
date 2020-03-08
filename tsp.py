# traveling salesman problem
# ant colonization
import sys
import math

class Tour(object):
    def __init__(self):
        self.text_name = str(sys.argv[1])
        self.int_string = []
        self.cities = []
        self.num_city = 0
        self.adj_matrix = []
        self.W = []

    def tour(self):
        self.storing_data()
        self.create_graph()

    def storing_data(self):
        # reading the files
        file = open(self.text_name, "r")
        lines = file.readlines() # reads all the lines in the file
        file.close()

        for num in range(len(lines)):
            self.int_string.append([int(i) for i in lines[num].split() if i.isdigit()])
        print (self.int_string)

        for i in range(len(self.int_string)):
            self.cities.append(City(self.int_string[i][0],self.int_string[i][1:]))
            print("city_id = %s  coordinate: %s "% (self.cities[i].city_id, self.cities[i].point))

    def distance(self,c1,c2):
        #x=[0] y=[1]
        x = c1[0] - c2[0]
        y = c1[1] - c2[1]
        total = math.sqrt(x**2 + y**2)
        return round(total)

    def create_graph(self):
        self.num_city = len(self.int_string)
        self.adj_matrix = [[math.inf for i in range(self.num_city)] for j in range(self.num_city)]
        edge = 0
        for i in range(self.num_city):
            for j in range(self.num_city):
                distance = self.distance(self.cities[i].point,self.cities[j].point)
                self.adj_matrix = Graph(edge,self.cities[i],self.cities[j],distance)
                self.adj_matrix.show_all()
                edge += 1

    #begining of find MST
    def find(self,parent,rank,vertex):
        if parent[vertex] == vertex:
            return parent[vertex]
        return self.find(parent, rank, parent[vertex])

    def union(self,parent,rank,root1,root2):
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root2] > rank[root1]:
            parent[root1]=root2
        else:
            parent[root1] = root2
            rank[root2] +=1

    def makeset(self,parent,rank,vertex):
        parent[vertex] = vertex
        rank[vertex] = 0

    def MST(self):
        A = []
        rank = [-1 for i in range(self.num_city)] #disjoint set rank
        parent = [-1 for i in range(self.num_city)] # disjoint set
        for i in range(len(points)):
            makeset(parent, rank,i)
        #mergesort the lower triangle

class City(object):
    def __init__(self,city_id,point):
        self.city_id = city_id # city number
        self.point = point #(x,y), where x is index 0 and y is index 1

class Graph(object):
    def __init__(self,edge,c1,c2,distance):
        self.edge = edge
        self.c1 = c1 #object city
        self.c2 = c2 #object city
        self.distance = distance

    def show_all(self):
        print("distance: %s c1: %s c2: %s edge: %s" % (self.distance, self.c1.point, self.c2.point, self.edge))

def main():
    tour = Tour()
    tour.tour()


main()
