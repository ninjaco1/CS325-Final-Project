# traveling salesman problem
# ant colonization
import sys
import math
import random

class Tour(object):
    def __init__(self):
        self.text_name = str(sys.argv[1])
        self.int_string = []
        self.cities = []
        self.num_city = 0
        self.adj_matrix = []
        self.W = []
        self.adj_list = [] # for MST everything but root
        self.MST
        self.T = []
        self.total_edge = 0

    def get_adj_matrix(self,i,j):
        return self.adj_matrix[i][j]

    def tour(self):
        self.storing_data()
        self.create_graph()
        self.MST()#find MST
        odd_vertices = self.odd_vertices()# find all odd vertex
        print("Odd vertexes in MSTree: ")#,odd_vertices)
        for vertex in odd_vertices:
            print(vertex.point)
        self.perfect_matching(odd_vertices)
        print("Edges in MST")
        print("Point [x,y]                  Distance")
        total_distance =0
        for i in range(len(self.MST)):
            self.MST[i].format()
            total_distance += self.MST[i].distance
        print("                           Total distance %s"% total_distance)
        #find euler tour


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
        self.total_edge = self.num_city ** 2 -1
        self.adj_matrix = [[math.inf for i in range(self.num_city)] for j in range(self.num_city)]
        edge = 0
        for i in range(self.num_city):
            for j in range(self.num_city):
                distance = self.distance(self.cities[i].point,self.cities[j].point)
                self.adj_matrix[i][j] = Graph(edge,self.cities[i],self.cities[j],distance)
                self.adj_matrix[i][j].show_all()
                edge += 1
        #make the lower triangle into one array
        for i in range(self.num_city):
            for j in range(self.num_city-(self.num_city-i)):
                self.W.append(self.adj_matrix[i][j])


    def mergesort(self,array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            #divide
            self.mergesort(left)
            self.mergesort(right)

            i = j = 0 #left and right
            k = 0 # main array
            #conquer
            while i < len(left) and j < len(right):
                if left[i].distance < right[j].distance:
                    array[k] = left[i]
                    i = i + 1
                else:
                    array[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                array[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                array[k] = right[j]
                j = j + 1
                k = k + 1

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

    def MST(self):#kruskal algorithms
        A = T = []
        rank = [-1 for i in range(self.num_city)] #disjoint set rank
        parent = [-1 for i in range(self.num_city)] # disjoint set
        for i in range(self.num_city):
            self.makeset(parent, rank,i)
        #mergesort the lower triangle
        self.mergesort(self.W)
        #line_number=1
        for i in range(len(self.W)):
            c1_index = c2_index = -1
            for k in range(self.num_city):
                for l in range(self.num_city):
                    if self.W[i].c1 == self.adj_matrix[k][l].c1:#city id needs to be fix
                        c1_index = self.adj_matrix[k][l].c1.city_id# node key value
                        break

            for k in range(self.num_city):
                for l in range(self.num_city):
                    if self.W[i].c2 == self.adj_matrix[k][l].c2:#point at that index
                        c2_index = self.adj_matrix[k][l].c2.city_id
                        break
            #print("c1_index: %s, c2_index: %s"%(c1_index,c2_index))
            root1 = self.find(parent,rank,c1_index)
            root2 = self.find(parent, rank,c2_index)
            if root1 != root2:
                A.append(self.W[i])#.key
                #T.append((self.W[i].c1,self.W[i].c2,self.W[i].distance))
                #print("%s.where came from: %s, where its going %s, distance: %s"%(line_number,self.W[i].c1.city_id,self.W[i].c2.city_id, self.W[i].distance))
                self.union(parent, rank, root1,root2)
                #line_number +=1

        print("Edges in MST")
        print("Point [x,y]                  Distance")
        total_distance =0
        for i in range(len(A)):
            A[i].format()
            total_distance += A[i].distance
        print("                           Total distance %s"% total_distance)

        '''
        self.adj_list = [[] for i in range(self.num_city)]
        for i in range(len(self.adj_list)-1):
            print("i+1: %s"%(i+1))
            j = A[i+1].c1.city_id
            print("i+1: %s, j: %s"%(i+1,j))
            self.adj_list[i+1].append(j)
            self.adj_list[j].append(i+1)
        print("adj_list: %s"%self.adj_list)
        '''
        #parent
        #print("parent %s"%parent)
        #print("length parent: %s"% len(parent))
        self.MST = A
        #self.T = T
        return A # the set of edges within the MST
        #print("A: %s"% A)

    def odd_vertices(self):
        #self.MST is the MST
        graph = {} #dictionary/hashtable
        vertices = []
        for edge in self.MST:
            if edge.c1 not in graph:
                graph[edge.c1] = 0

            if edge.c2 not in graph:
                graph[edge.c2] = 0

            graph[edge.c1] += 1
            graph[edge.c2] += 1

        for vertex in graph:
            if graph[vertex]%2==1:
                vertices.append(vertex)#inserts hashtable
        return vertices



    def perfect_matching(self,odd_vertices):
        random.shuffle(odd_vertices)
        #c1,c2,distance for mst
        #odd: city object
        while odd_vertices:
            v = odd_vertices.pop()#c1
            distance = math.inf
            u=1
            close =0
            for u in odd_vertices:
                if v != u and self.adj_matrix[v.city_id][u.city_id].distance < distance:
                    distance = self.adj_matrix[v.city_id][u.city_id].distance
                    close = u
            self.MST.append(Graph(self.total_edge,v,close,distance))
            self.total_edge +=1
            odd_vertices.remove(close)

    def euler_tour(self):
        pass


class City(object):
    def __init__(self,city_id,point):
        self.city_id = city_id # city number
        self.point = point #(x,y), where x is index 0 and y is index 1

class Graph(object):
    def __init__(self,edge,c1,c2,distance):
        self.edge = edge # key value
        self.c1 = c1 #object city
        self.c2 = c2 #object city
        # self.c1_id = c1_id
        # self.c2_id = c2_id
        self.distance = distance

    def show_all(self):
        print("distance: %s c1: %s c2: %s edge: %s" % (self.distance, self.c1.point, self.c2.point, self.edge))
    def format(self):
        print("%s(%s) - %s(%s)      %s"%(self.c1.point,self.c1.city_id, self.c2.point,self.c2.city_id, self.distance))

def main():
    tour = Tour()
    tour.tour()


main()
