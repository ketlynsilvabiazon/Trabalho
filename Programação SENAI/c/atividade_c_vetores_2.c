#include <stdio.h>

int main() {
    int vetor[10];
    int i;
    
    for(i = 0; i < 10; i++){
        vetor[i] = i + 1;
    
    }
    printf("Numeros pares:\n");
    
    for(i = 0; i < 10; i++){
        if (vetor[i] % 2 == 0){
            printf("%d", vetor[i]);
        }
    }
    return 0;
}