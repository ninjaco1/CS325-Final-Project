#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <vector>
#include <limits>
#include <time.h>
#include <algorithm>

//Struct for the vertices
struct vertice{
   int x;
   int y;
   int id;
};

//Struct for the edges
struct edge{
   int departure_id;
   int departure_x;
   int departure_y;

   int arrival_id;
   int arrival_x;
   int arrival_y;

   int weight;
};

void merge(struct edge** array,int index, int left, int middle, int right){
   int i = left;
   int j = middle + 1;
   int k = 0;
   struct edge test[(right - left) + 1];
   while(i <= middle || j <= right){
      if(i > middle){
         test[k] = array[index][j];
         k++;
         j++;
      }
      else if(j > right){
         test[k] = array[index][i];
         k++;
         i++;
      }
      else if(array[index][i].weight > array[index][j].weight){
         test[k] = array[index][j];
         k++;
         j++;
      }
      else{
         test[k] = array[index][i];
         k++;
         i++;
      }
   }

   for(int m = left; m < right + 1; m++){
      array[index][m] = test[m - left];
   }
}

// void sort(struct edge** array, int index, int left, int right){
//    if(left >= right)
//       return;
//    else{
//       int middle = (left + right)/2;
//       sort(array,index,left,middle);
//       sort(array,index,middle + 1,right);
//       merge(array,index,left,middle,right);
//    }
// }

int distance_calculator(int start, int end, std::vector<struct vertice>* vertice){
   int x = vertice->at(start).x - vertice->at(end).x;
   x = x * x;

   int y = vertice->at(start).y - vertice->at(end).y;
   y = y * y;

   int dummy = (int) (sqrt(x+y) + 0.5);

   return dummy;
}

bool key(struct edge a, struct edge b){
   return a.weight < b.weight;
}

int RNN2(int start, int v, std::vector<struct vertice> vertice, std::vector<int> &temp_path, bool checked[], struct edge** edge){
   checked[start] = true;
   int best_v = -1;
   int best_distance = std::numeric_limits<int>::max();
   int counter = 0;
   for(int i = 0; i < v; i++){
      if(checked[edge[start][i].arrival_id] == false){
         counter++;
         best_distance = edge[start][i].weight;
         best_v = edge[start][i].arrival_id;
         break;
      }
   }

   if(counter == 0){
      temp_path.push_back(temp_path[0]);
      return distance_calculator(temp_path[0],start,&vertice);
   }
   else{
      temp_path.push_back(best_v);
      return best_distance + RNN2(best_v,v,vertice,temp_path,checked,edge);
   }
}

int RNN(int start, int v, std::vector<struct vertice> vertice, std::vector<int> &temp_path, struct edge** edge){
   bool checked[v];
   for(int i = 0; i < v; i++){
      checked[i] = false;
   }
   temp_path.push_back(start);
   return RNN2(start,v,vertice,temp_path,checked,edge);
}


//main function
int main(int argc, char* argv[]){
   clock_t begin = clock();
   srand(NULL);

   //Checks to make sure file is there
   FILE *file;
   file = fopen(argv[1],"r");
   if(file == NULL){
      printf("No file found.\n");
      exit(0);
   }

   //Checks total number of vertices in file
   int v = 0;
   for(char q = getc(file); q != EOF; q = getc(file)){
      if(q == '\n')
         v++;
   }
   fclose(file);
   file = fopen(argv[1],"r");

   //Stores data of vertices
   std::vector<struct vertice> vertice;
   for(int i = 0; i < v; i++){
      struct vertice temp;
      fscanf(file,"%d",&temp.id);
      fscanf(file,"%d",&temp.x);
      fscanf(file,"%d",&temp.y);
      vertice.push_back(temp);
   }
   fclose(file);

   // for(int i = 0; i < v; i++){
   //    printf("%d %d %d\n",vertice[i].id,vertice[i].x,vertice[i].y);
   // }

   int e = (v * (v - 1))/2;

   // //Stores distance of edges
   // //std::vector< std::vector<struct edge> > edge[0];
   // std::vector<struct edge> edge[1];
   // int k = 0;
   // for(int i = 0; i < v; i++){
   //    for(int j = 0; j < v; j++){
   //       if(i != j){
   //          std::vector<struct edge> temp;
   //          struct edge temp1;
   //
   //
   //          temp1.departure_x = vertice[i].x;
   //          temp1.departure_y = vertice[i].y;
   //          temp1.arrival_x = vertice[j].x;
   //          temp1.arrival_y = vertice[j].y;
   //          temp1.weight = distance_calculator(i,j,vertice);
   //
   //          temp.push_back(temp1);
   //          edge[i].push_back(temp);
   //
   //       }
   //    }
   //    //edge.push_back();
   // }

   printf("\nCreating Edges...\n");
   struct edge** edge = new struct edge*[v];
   for(int i = 0; i < v; i++){
      edge[i] = new struct edge[v];
   }
   for(int i = 0; i < v; i++){
      for(int j = 0; j < v; j++){
            struct edge* E = &edge[i][j];
            E->departure_id = i;
            E->departure_x = vertice[i].x;
            E->departure_y = vertice[i].y;
            E->arrival_id = j;
            E->arrival_x = vertice[j].x;
            E->arrival_y = vertice[j].y;
            E->weight = distance_calculator(i,j,&vertice);
      }
   }
   printf("Edges Complete\n");

   printf("\nSorting...\n");
   for(int i = 0; i < v; i++){
      //sort(edge,i,0,v - 1);
      std::sort(edge[i], edge[i] + v, key);
   }
   printf("Sorting Complete\n");

   // for(int i = 0; i < v; i++){
   //    for(int j = 0; j < v; j++){
   //       printf("Depart:%d Arrive:%d Distance:%d\n",edge[i][j].departure_id,edge[i][j].arrival_id,edge[i][j].weight);
   //    }
   //    printf("\n");
   // }

   std::vector<int> best_path;
   int best_index = -1;
   int best_distance = std::numeric_limits<int>::max();
   printf("\n");
   for(int i = 0; i < 100; i++){
      printf("Working on trial %d...\n",i + 1);
      std::vector<int> temp_path;
      int temp_index = rand() % v;
      int temp_distance = RNN(temp_index,v,vertice,temp_path,edge);
      if(temp_distance < best_distance){
         best_distance = temp_distance;
         best_index = temp_index;
         for(int i = 0; i < v; i++){
            best_path.push_back(temp_path[i]);
            //printf("%d\n",temp_path[i]);
            //printf("hello\n");
         }
      }
   }
   clock_t end = clock();
   double t = (double)(end - begin)/CLOCKS_PER_SEC;
   printf("\nbest distance: %d\n",best_distance);
   printf("best time: %f\n",t);


   char dummy[100];
   std::string tour = ".tour";
   char b[tour.size()];
   strcpy(b,tour.c_str());

   strcpy(dummy,argv[1]);
   strcat(dummy,b);
   FILE *outfile;
   outfile = fopen(dummy,"w+");
   fprintf(outfile,"%d",best_distance);
   fprintf(outfile,"%s","\n");
   for(int i = 0; i < v; i++){
      fprintf(outfile,"%d",best_path.at(i));
      fprintf(outfile,"%s","\n");
   }
   fclose(outfile);
}
