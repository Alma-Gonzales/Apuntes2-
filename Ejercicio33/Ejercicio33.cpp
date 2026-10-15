//Apunte 1
//Alma Leticia Douglas Gonzales Guilbert

#include <iostream>
using namespace std;

int main()
{
	//Arreglos con valores iniciales
	int c[] = { 12,3,27,16,4,51,8,40 };

	cout << c[0] << endl;
	cout << c[1] << endl;
	cout << c[2] << endl;
	cout << c[3] << endl;
	cout << c[4] << endl;
	cout << c[5] << endl;
	cout << c[6] << endl;
	cout << c[7] << endl;

	//Arreglo sin valores iniciales

	string materia[5];

	cout << "Ingresa la materia 1: ";
	cin >> materia[0];

	cout << "Ingresa la materia 2: ";
	cin >> materia[1];

	cout << "Ingresa la materia 3: ";
	cin >> materia[2];

	cout << "Ingresa la materia 4: ";
	cin >> materia[3];

	cout << "Ingresa la materia 5: ";
	cin >> materia[4];

	cout << materia[0] << endl;
	cout << materia[1] << endl;
	cout << materia[2] << endl;
	cout << materia[3] << endl;
	cout << materia[4] << endl;

	int i;
	cout << "Ingresa el numero de la mataria que quieres mostrar: ";
	cin >> i;
	cout << materia[i - 1];

	return 0;
}