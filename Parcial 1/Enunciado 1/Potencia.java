/* Autor: Jesus Bandez 1710046
Implementacion de la funcion potencia en Java. Se hacen dos implementaciones: Iterativa y
recursiva.*/

public class Potencia {

/* Implementacion recursiva de la funcion potencia:
    Parametros:
        a: int no negativo que es la base de la potencia
        b: int no negativo que es el exponente de la potencia
    Retorna:
        El resultado de multiplicar a, b veces
*/
public static int potenciarRecursivo(int a, int b) {
    // Se asume que a y b son numeros no negativos.

    // Si a y b son ambos 0, se arroja una exception
    if (a == 0 && b == 0){
        throw new RuntimeException("La potencia de 0 a la 0 no esta definida");
    } else if (a<0 || b<0){
        throw new RuntimeException("La base y el exponente deben ser no negativos");
    }

    // Si el exponente es 0, se retorna 1
    if (b==0){
        return 1;
    
    // Si el exponente no es 0, entonces se hace el paso recursivo
    } else {
        return a * potenciarRecursivo(a, b-1);
    }
}

/* Implementacion recursiva de la funcion potencia:
    Parametros:
        a: int no negativo que es la base de la potencia
        b: int no negativo que es el exponente de la potencia
    Retorna:
        acc: int que es el resultado de multiplicar a, b veces
*/
public static int potenciarIterativo(int a, int b) {
    // Se asume que a y b son numeros no negativos.

    // Si a y b son ambos 0, se arroja una exception
    if (a == 0 && b == 0){
        throw new RuntimeException("La potencia de 0 a la 0 no esta definida");
    } else if (a<0 || b<0){
        throw new RuntimeException("La base y el exponente deben ser no negativos");
    }

    // variable acumulador que retorna el valor calculado
    int acc = 1;

    // Mientras el exponente se mayor a 0, se multiplica
    // el acumulador por la base y se reduce el valor de 
    // b
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
    base = 4; exponente = 3;   

    System.out.println(potenciarRecursivo(base, exponente));
    System.out.println(potenciarIterativo(base, exponente));
}
}