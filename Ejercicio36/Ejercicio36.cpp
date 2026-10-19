//Apunte 1 19/10/2026
//Alma Leticia Dpuglas Gonzales Guilbert
//Valores pseudo-aleatorios

#include <iostream>
#include <cstdlib> //Funciones rad()
#include <ctime> //tiempo del sistema
using namespace std;

int main()
{   
	//semilla
	srand(time(NULL));

	int num; 

	num = rand(); // Genra un valor aleatorio y lo asigna a 'num' 
	cout << "Valor pseudo-aleatorio: " << num << endl;

	//valores entre 0 y 10
	num = rand() % 11;
	cout << "Valores entre 0 - 10: " << num << endl;

	//Valor entre 1 y 10 
	num = rand() % 10 + 1;
	cout << "Valores entre 1 - 10: " << num << endl;

	//Valor entre 5 y 15 
	num = rand() % 11 + 5;
	cout << "Valores entre 5 - 15: " << num << endl;

	//Valor entre 180 y 220 
	num = rand() % 41 + 180;
	cout << "Valores entre 1 - 10: " << num << endl;



	return 0; 
}