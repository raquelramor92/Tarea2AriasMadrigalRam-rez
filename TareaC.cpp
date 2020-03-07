#include "iostream"
#include <thread>
#include <ctime> 
#include <stdlib.h>
//#include <wiringPi.h>


unsigned  t00, t01;
unsigned t02, t03;

using namespace std;

void Gener_Array(int array[100], int conta){
    for(int i = 0; i < 100; ++i)
        {
            array[i] = conta;
            ++conta;
        }
    }

int main()

{
	//wiringPiSetup();
	//pinMode(0, OUTPUT);
	//digitalWrite(0, HIGH);
	//delay(500);

	
	

    int array[100] = {0};
    int conta = 0;
	Gener_Array(array,conta);
	
	// Hilo 1
	
	t00 = clock();
	
	thread t0 ([&array]{
        for(unsigned int i = 0; i < 100; ++i)
        {
            array[i] = array[i]*array[i];
            
        }
        });
        
    t0.join();
    
    t01 = clock();
    
    double time = (double(t01-t00)/CLOCKS_PER_SEC);   
    cout << "Tiempo: " << time << endl;

    
    for (int i = 0; i < 100; i++)
    {
            cout<<array[i]<<endl;
    }
    
    
    
	// Cuatro hilos

    t02 = clock();

    thread t1 ([&array]{
        for(unsigned int i = 0; i < 25; ++i)
        {
            array[i] = array[i]*array[i];
            
        }
        });
    
    thread t2 ([&array]{
        for(unsigned int m = 25; m < 50; ++m)
        {
            array[m] = array[m]*array[m];
            
        }
        });
    
    thread t3 ([&array]{
        for(unsigned int n = 50; n < 75; ++n)
        {
            array[n] = array[n]*array[n];
            
        }
        });
    
    thread t4 ([&array]{
        for(unsigned int e = 75; e < 100; ++e)
        {
            array[e] = array[e]*array[e];
            
        }
        });
    
    t2.join();
    t1.join();
    t3.join();
    t4.join();
    
    t03 = clock();
    
    double time2 = (double(t03-t02)/CLOCKS_PER_SEC);   
    cout << "Tiempo: " << time2 << endl;
    
   
    for (int i = 0; i < 100; i++)
    {
            cout<<array[i]<<endl;
    }
    
    
    
    
    return 0;
    
    
}
