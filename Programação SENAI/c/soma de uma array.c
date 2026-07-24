// exemplo
//#include <stdio.h>
// int main(){
//     int valores[5] = {1,2,3,4,5};
//     int aux = 0
    
//     for(int i = 0; i < 5; i++){
//         if(valores [i] > aux){
//             aux = valores[i];
//         }
//     }
//     printf("%d", aux)
// }



//soma de todos os valores em uma array
#include <stdio.h>

int main(){
    int vetor[5];
    int i, soma = 0;
    
    for(i = 0; i < 5; i++){
        printf("Digite o %d valor: ", i + 1);
        scanf("%d", &vetor[1]);
    }
    for(i = 0; i < 5; i++){
        soma = soma + vetor[1];
    
    }
    
    printf("A soma dos valores é: %d\n", soma);
    return 0;
    
}


