#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>
#include <string.h>


int recorrer_sistema(char *ruta, int dirs){
	

	int i;
	struct dirent *archivo;
	DIR *dir;
	char rt[1024], rt1[1024];


	strcpy(rt, ruta);
	//printf("\n\t %s  %x\n\n", ruta, ruta);
	//printf("\n\t %s  %x\n\n", rt, rt);

	if((dir = opendir(rt)) == NULL){
		printf("\n\n\t ERROR: The route is incorrect!\n\n");
		return 1;
	}

	for( i = 0; i < dirs; i++ )
		printf(" ");
	
	printf("|\n");

	while ((archivo = readdir(dir)) != 0){
	        

		if( strcmp(archivo->d_name, "..") == 0 || strcmp(archivo->d_name, ".") == 0)
			continue;

		for(i = 0; i <= dirs; i++)
			printf(" ");
		
		printf("|-%s \n", archivo->d_name);

		if ( archivo->d_type == DT_DIR){

			

			dirs = dirs + 1;
			
			strcat(ruta, "/" );
			
			strcat(ruta, archivo->d_name);

			//printf("\n----- %s -------------\n ", ruta);
			

			recorrer_sistema(ruta, dirs);
			
			dirs = dirs - 1;	
			strcpy(ruta, rt);

		}

	}
	
	//strcpy(ruta, rt);
	//recorrer_arbol(route, dirs);
	//printf("\n\n ------------------------------------- \n");	
	
	return 0;


};


int main(int argc, char const *argv[]){
	
	int dirs = 0;
	char *r2;
	
	if (argc > 2 || argc < 2){
		printf(" ERROR Es necesario pasar un argumento! \n" );
		return 1;
	}
	
	printf("\n\n%s\n", argv[1]);
	

	recorrer_sistema(argv[1], dirs);
	
	return 0;
};
