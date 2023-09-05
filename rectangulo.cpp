#include <iostream>

class Rectangulo {
private:
    double longitud;
    double ancho;

public:
    
    Rectangulo(double l, double a) : longitud(l), ancho(a) {}

    
    double calcular_area() {
        return longitud * ancho;
    }

  
    double calcular_perimetro() {
        return 2 * (longitud + ancho);
    }

   
    void cambiar_longitud(double nueva_longitud) {
        longitud = nueva_longitud;
    }

   
    void cambiar_ancho(double nuevo_ancho) {
        ancho = nuevo_ancho;
    }
};

int main() {
    
    Rectangulo Rectangulo_inicial(9, 6);

 
    std::cout << "el area del rectángulo es: " << Rectangulo_inicial.calcular_area() << std::endl;

    std::cout << "el perímetro del rectángulo es: " << Rectangulo_inicial.calcular_perimetro() << std::endl;

    return 0;
}
