/*
- Realizar un programa que simule la boleta de un estudiante. 
- El programa debera preguntar cuantas materias desea ingresar. 
- El nombre de las materias y la calificacion de las materias deberan
almacenarse en un arreglo string y otro int respectivamente. 
 - Las calificaiones de la materia se deberan generar de forma aleatoria 
 en un rango de 5 a 10 
 - Al final debera mostrar la suma y el promedio de las calificaciones. 
 - Imprimir un grafico de frecuencia por cada calificacion y el promedio final
 Ejemplo: 
 Materia 1 , 9 : *******
 Materia 2, 5 : ****
 Materia 3 ,7 : *********

*/


#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <iomanip>

using namespace std;

int main() {
    int cantMat;

    cout << "Ingrese cantidad de materias: ";
    cin >> cantMat;

    if (cantMat <= 0 || cantMat > 100) {
        cout << "Ingresa una cantidad entre 1 y 100." << endl;
        return 1;
    } 

    string materias[100];
    int notas[100];

    
    srand(time(0));

    int suma = 0;

    cin.ignore(10000, '\n');


    for (int i = 0; i < cantMat; i++) {
        cout << "\nNombre de la materia " << i + 1 << ": ";
        getline(cin, materias[i]);

        // Calificacion aleatoria entre 5 y 10
        notas[i] = rand() % 6 + 5;

        suma += notas[i];
    }

    double promedio = (double)suma / cantMat;

    for (int i = 0; i < cantMat; i++) {
        cout << materias[i] << " - "
            << notas[i] << endl;
    }

    cout << "\nSuma de calificaciones: " << suma << endl;

    cout << fixed << setprecision(2);
    cout << "Promedio final: " << promedio << endl;

    cout << "\n Frecuencia de calificaion" << endl;

    for (int cal = 5; cal <= 10; cal++) {
        int frecuencia = 0;

        for (int i = 0; i < cantMat; i++) {
            if (notas[i] == cal) {
                frecuencia++;
            }
        }

        cout << cal << " : ";

        for (int j = 0; j < frecuencia; j++) {
            cout << "*";
        }

        cout << endl;
    }
    cout << "\n Grafica por Materia " << endl;
    

    for (int i = 0; i < cantMat; i++) {
        cout << materias[i] << ", "
            << notas[i] << " : ";

        for (int j = 0; j < notas[i]; j++) {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}