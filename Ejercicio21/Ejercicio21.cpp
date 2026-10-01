/* Alma Leticia Douglas Gonzales Guilbert
Un almacen de pedidos por correo vende cinco productos,
los precios son los siguientes:
-producto1: $2.98 
-producto2: $4.50
-producto3: $9.98
-producto4: $4.49
-producto5: $6.87

Escriba un programa que solicite el numero del producto y la cantidad vendida.
El programa debe determinar el precio de venta de cada producto, calcular y 
mostrar el valor total del producto.

*/

#include<iostream>
using namespace std;

int main() {
	
	int numPro, canVen;
	float preVen, valTot;

	cout << "Ingrese el numero del producto 1 al 5: ";
	cin >> numPro;
	cout << "Ingrese la cantidad vendida: ";
	cin >> canVen;

	switch (numPro) {
	case 1: preVen = 2.98; 
		break;
	case 2: preVen = 4.50;
		break;
	case 3: preVen = 9.98;
		break;
	case 4: preVen = 4.49;
		break;
	case 5: preVen = 6.87;
		break;
	default: preVen = 0;
		cout << "Error: El producto no existe" << endl; 
		break;
	}

	cout << "El precio de venta del producto " << numPro << ": $" << preVen << endl;
	valTot = canVen * preVen;
	cout << "Total de la venta: $ " << valTot << endl;


	return 0;
}