#ifdef linux                   /* __unix__ is usually defined by compilers targeting Unix systems */

    #include <stdlib.h>
    #include <stdio.h>
	#include <unistd.h>

#elif _WIN32    /* _Win32 is usually defined by compilers targeting 32 or   64 bit Windows systems */

    #include <windows.h>
    #include <stdio.h>

#endif

int main()
{

#ifdef _WIN32
	SYSTEM_INFO siSysInfo;
 
    // Copy the hardware information to the SYSTEM_INFO structure. 
 
    GetSystemInfo(&siSysInfo); 
	int numCPU = siSysInfo.dwNumberOfProcessors;
#endif

#ifdef linux
	int numCPU = sysconf(_SC_NPROCESSORS_ONLN);
#endif
	
	printf("El numero de procesadoresde tu maquina es: %i\n", numCPU);
	
	return 0;
}