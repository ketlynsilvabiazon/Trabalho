#include <stdio.h>

int main() {
    int vetor[10];
    int i;
    
    for(i = 0; i < 10; i++){
        printf("Digite o %d numero: ", i + 1);
        scanf("%d", &vetor[i]);
    }
    printf("\nNumeros digitados:\n");
    for(i = 0; i < 10; i++){
        printf("%d ", vetor[i]);
    }
    return 0;
}