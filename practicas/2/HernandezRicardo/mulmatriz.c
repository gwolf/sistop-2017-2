#include <stdio.h>
#include <stdlib.h>

int main(){

     int **matriz; 

     matriz = (int**) calloc (3, sizeof(int*)); //reserva memoria para un apuntador 
     
     if (matriz == NULL){
          printf("No se puede reservar memoria. \n");
          exit(-1);
     }

     for (int i=0; i<3; i++){
     
          if((matriz[i] = (int*) calloc (3, sizeof(int))) == NULL){
          printf("No se puede reservar memoria. \n");
          exit(-1);
          }
     }

     for(int i = 0; i < 3; i++)
          for(int j = 0; j < 3; j++)
               matriz[i][j] = i*j;  //Llenarlo automático
               //scanf("%d",&matriz[i][j]);  //pedir valores

     for(int i = 0; i < 3; i++){
          for(int j = 0; j < 3; j++)
               printf("\t%d",matriz[i][j]);
          printf("\n");
     }

     for(int i=0; i < 3; i++) //for para liberar memoria (columnas)
          free(matriz[i]); 
     
     free(matriz); //libera la memoria 
     
     
               
}
