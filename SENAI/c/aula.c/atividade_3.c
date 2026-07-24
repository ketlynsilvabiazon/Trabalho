#include <stdio.h>

float calcular(float n1, float n2, char op)
{
 if(op == '+')
 return n1 + n2;
 else if(op == '-')
 return n1 - n2;
 else if(op == '*')
 return n1 * n2;
 else if(op == '/')
 {
 if(n2 != 0)
 return n1 / n2;
 else
 {
 printf("Erro: divisao por zero!\n");
 return 0;
 }
 }

 return 0;
}

int main()
{
 float n1, n2, resultado;
 char op;

 printf("Digite o primeiro numero: ");
 scanf("%f", &n1);

 printf("Digite a operacao (+ - * /): ");
 scanf(" %c", &op);

 printf("Digite o segundo numero: ");
 scanf("%f", &n2);

 resultado = calcular(n1, n2, op);

 printf("Resultado: %.2f", resultado);

 return 0;
}

