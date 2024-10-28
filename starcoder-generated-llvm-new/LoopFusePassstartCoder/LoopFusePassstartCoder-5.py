
```c
#include <stdio.h>

int main() {
    unsigned long int i, j;
    int arr1[100000], arr2[100000], result[100000];
    for (i = 0; i < 100000; i++) {
        arr1[i] = i+1;
        arr2[i] = 2*(i+1);
    }
    for (j = 0; j < 100000; j++) {
        arr1[j] += 1;
    }
    for (i = 0; i < 100000; i++) {
        arr2[i] += 2;
    }
    for (i = 0; i < 100000; i++) {
        result[i] = arr1[i] + arr2[i];
    }
    for (i = 0; i < 100000; i++) {
        printf("%d ", result[i]);
    }
    return 0;
} 
```

