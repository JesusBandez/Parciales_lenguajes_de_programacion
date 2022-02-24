/* Autor: Jesus Bandez 1710046
Implementacion de la funcion potencia en Java. Se hacen dos implementaciones: Iterativa y
recursiva.*/

public class Potencia {

public static int potenciarRecursivo(int a, int b) {
    if (b==0){
        return 1;
    } else {
        return a * potenciarRecursivo(a, b-1);
    }
}

public static int potenciarIterativo(int a, int b) {
    int acc = 1;
    while (b > 0){
        acc = acc*a;
        b--;
    }
    return acc;
}
public static void main(String[] args) {
    // Se imprimen por salida estandar las respuestas de ambas
    // funciones para comprobar que esten correctas
    int base, exponente;
    base = 4;
    exponente = 3;
    System.out.println(potenciarRecursivo(base, exponente));
    System.out.println(potenciarIterativo(base, exponente));


}
}