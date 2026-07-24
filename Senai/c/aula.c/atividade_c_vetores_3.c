#include <stdio.h>

int main() {
    int vetor[10];
    int i, valor = 10;
    
    for(i = 0; i < 10; i++){
        vetor[i] = valor;
        valor += 10;
    
    }
    printf("Ordem inversa:\n");
    
    for(i = 9; i >= 0; i--){
        if (vetor[i] % 2 == 0){
            printf("%d", vetor[i]);
        }
    }
    return 0;
}