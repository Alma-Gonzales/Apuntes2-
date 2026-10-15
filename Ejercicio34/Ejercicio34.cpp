//Apunte 2 - Arreglos con Ciclos
//Alma Leticia Douglas Gonzales Guilbert

#include <iostream>
using namespace std;

int main()
{
	//Arreglos con valores iniciales
	int c[] = { 12,3,27,16,4,51,8,40 };

	for (int i = 0; i < 8; i++) {
		cout << c[i] << endl;
	}

	//Arreglo sin valores iniciales

	string materia[5];
	
	for (int i = 0; i < 5; i++) {
		cout << "Ingresa la materia " << i + 1 << ": ";
		cin >> materia[i];
	}
	for (int i = 0; i < 5; i++) {
		cout << materia[i] << ", ";
	}

	
	return 0;
}