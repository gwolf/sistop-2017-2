//Schwuchow Machorro Antonio Programa ejemplo de threads para practica 2
#include <iostream>
#include <process.h>
#include <windows.h>
using namespace std;

void test(void *param)
{
    cout << "In thread function" << endl;
    Sleep(1000); // sleep for 1 second
    cout << "Thread function ends" << endl;
    _endthread();
}


int main()
{
    cout << "Starting thread" << endl;
    cout << _beginthread(test,0,NULL);
    cout << "Main ends" << endl;
    return 0;
}

//fuente: http://www.bogotobogo.com/cplusplus/multithreading_win32A.php
