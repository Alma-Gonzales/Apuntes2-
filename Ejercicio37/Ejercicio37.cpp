//Apunte 2 19/10/2026
//Alma Leticia Dpuglas Gonzales Guilbert
//Arreglo con valores aleatorios

#include <iostream>
#include <cstdlib> //Funciones rad()
#include <ctime> //tiempo del sistema
using namespace std;

int main() {

	//valores aleatorios entre 50 y 100
	srand(time(0));

	int promedio, suma = 0;
	int Aleatorios[5];

	for (int i = 0; i < 5; i++) {
		Aleatorios[i] = rand() % 51 + 50;
		suma = suma + Aleatorios[i];
		cout << Aleatorios[i] << ", ";
	}

	promedio = suma / 5;
	cout << "\nEl promedio de los valores es: " << promedio << endl;


	return 0;
}