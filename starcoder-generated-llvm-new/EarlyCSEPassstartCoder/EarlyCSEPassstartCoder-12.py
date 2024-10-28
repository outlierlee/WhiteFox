
```c
#include <stdio.h>

int main() {
    int rows = 10;
    for(int i=0; i<rows; i++){
        for(int j=0; j<=i; j++){
            printf("*");
        }
        printf("\n");
    }

    printf("\n");

    int i, j, k, n=5;
    for(i=0; i<n; i++){
        for(j=1; j<=n-i; j++){
            printf(" ");
        }
        for(k=0; k<(2*i+1); k++){
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
```
