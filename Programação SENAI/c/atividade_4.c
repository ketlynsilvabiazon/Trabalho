#include <stdio.h>

char conceitoAluno(float nota)
{
 if(nota >= 9)
 return 'A';
 else if(nota >= 7)
 return 'B';
 else if(nota >= 5)
 return 'C';
 else
 return 'D';
}

int main()
{
 float nota;

 printf("Digite a nota: ");
 scanf("%f", &nota);

 printf("Conceito: %c", conceitoAluno(nota));

 return 0;
}

