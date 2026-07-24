
#include <stdio.h>

int verifcarnumero (int numero)
{
 if (numero > 0)
    printf("Positivo");
 else if (numero < 0)
    printf("Negativo");
 else
    printf("Zero");
return 0;

}
int main(){
 int numero;
 
 printf("Digite um numero: ");
 scanf("%d", &numero);
 verifcarnumero(numero);
 return 0;
}
