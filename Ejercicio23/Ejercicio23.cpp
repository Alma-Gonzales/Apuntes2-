//Apunte 1 - Area y perimetro de un circulo 
//6 de octubre 2026
//Alma Leticia Douglas Gonzales Guilbert

#define _USE_MATH_DEFINES // Solucion con M_PI
#include<iostream>
#include<cmath> //Incluye funciones matematicas
#include<iomanip> //libreria para formatos de salida

using namespace std;

int main() {

	double radio, area, perimetro;
	cout << "Ingresa el radio del circulo: "; cin >> radio;
	//Calcular el area sin funciones matematicas

	area = 3.14151987552 * radio * radio;
	cout << "El area (sin funciones): " << area << endl;
	cout << "El area (sin funciones con formato): " << fixed << setprecision(1) << area << endl;

	area = M_PI * pow(radio, 2);
	cout <<"El area (con funciones con formato): " <<fixed << setprecision(1) << area << endl;

	perimetro = 2 * radio * M_PI;
	cout << "El perimetro es: " << fixed << setprecision(1) << perimetro << endl;

	return 0;
}