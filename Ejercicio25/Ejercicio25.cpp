//Apunte 3 Calcular el iva 16% de una venta, subtotal y total.
//Solicitar precio y cantidad del producto
//Alma Leticia Douglas Gonzales Guilbert

#include<iostream>
#include<iomanip>

using namespace std;

int main() {

	float precio, iva, subtotal, total;
	int cantidad;

	cout << "Precio del producto $: "; cin >> precio;
	cout << "Cantidad del Producto $: ", cin >> cantidad;

	subtotal = precio * cantidad;
	iva = subtotal * 0.16;
	total = subtotal + iva;

	cout << "Subtotal $: " << fixed << setprecision(2) << subtotal << endl;
	cout << "IVA $: " << fixed << setprecision(2) << iva << endl;
	cout << "Total $: " << fixed << setprecision(2) << total << endl;

	return 0;
}