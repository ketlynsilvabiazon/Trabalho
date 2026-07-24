
#include <stdio.h>

int classificaridade (int idade)
{
 if (idade <= 12)
    printf("Criança");
 else if (idade <= 17)
    printf("Adolescente");
 else if (idade <= 59)
    printf("Adulto");
 else
    printf("Idoso");
return 0;

}
int main(){
 int idade;
 
 printf("Digite a idade: ");
 scanf("%d", &idade);
 
 classificaridade(idade);
 
 return 0;
}
