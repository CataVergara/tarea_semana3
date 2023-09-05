#include <iostream>
#include <cmath>

class Circulo {
private:
    double radio;

public:
   
    Circulo(double r) {
        radio = r;
    }

 
    double calcular_area() {
        return M_PI * radio * radio;
    }

    
    double calcular_perimetro() {
        return 2 * M_PI * radio;
    }

    
    void cambiar_radio(double radio_nuevo) {
        radio = radio_nuevo;
    }
};

int main() {

    Circulo Circulo_inicial(9);

    
    double area = Circulo_inicial.calcular_area();
    std::cout << "el area del círculo es: " << area << std::endl;

    
    double perimetro = Circulo_inicial.calcular_perimetro();
    std::cout << "el perímetro del círculo es: " << perimetro << std::endl;

    return 0;
}
