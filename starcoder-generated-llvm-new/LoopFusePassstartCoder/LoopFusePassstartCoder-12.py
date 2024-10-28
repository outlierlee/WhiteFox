
```c
#include <stdio.h>

int main() {
    int i, j, k;
    int array1[10], array2[10], array3[10];

    // Initialize arrays
    for (i = 0; i < 10; i++) {
        array1[i] = i;
        array2[i] = i * 2;
    }

    for (i = 0; i < 10; i++) {
        array1[i] *= i;
        array2[i] *= i;
    }

    for (i = 0; i < 10; i++) {
        array1[i] *= i;
        array2[i] *= i;
    }

    for (i = 0; i < 10; i++) {
        array3[i] = array1[i] + array2[i];
    }

    for (i = 0; i < 10; i++) {
        printf("%d ", array3[i]);
    }

    return 0;
}
```

