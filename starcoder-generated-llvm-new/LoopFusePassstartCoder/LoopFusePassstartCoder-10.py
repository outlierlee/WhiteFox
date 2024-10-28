
```c
#include <stdio.h>

int main() {
    int i, j, k;
    int array1[10], array2[10], array3[10];

    // Initialize arrays
    for (i = 0; i < 10; i++) {
        array1[i] = i * 2 + 1;
        array2[i] = i * 3 + 2;
    }

    // First loop: perform some operations on array1
    for (j = 0; j < 10; j++) {
        array1[j] += 1;
    }

    // Second loop: perform some operations on array2
    for (k = 0; k < 10; k++) {
        array2[k] += 2;
    }

    // Use the results of the loops
    for (i = 0; i < 10; i++) {
        array3[i] = array1[i] + array2[i];
        printf("%d ", array3[i]);
    }

    return 0;
}
```

