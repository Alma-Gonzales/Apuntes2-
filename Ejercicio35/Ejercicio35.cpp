//Apunte 3 - Arreglos con Ciclos
//Alma Leticia Douglas Gonzales Guilbert
//Pedir al usiario 5 numeros enteros, guardalos en un arreglo y 
//mostrarlos en orden inverso al que fueron ingresados.
//utiliza ciclos para pedir y mostrar los valores. 

#include <iostream>
using namespace std;

int main() {
	int num[5];

		for (int i = 0; i < 5; i++) {
			cout << "Ingrese el numero " << i + 1 << ": ";
			cin >> num[i];
	}
		cout << " Numeros en orden inverso: " << endl;

		for (int i = 4; i >= 0; i--){
			cout << num[i] << ",";
		}

	return 0;
}