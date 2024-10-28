
```c
#include <stdio.h>

int main() {
    int i, j, k;
    int array1[5], array2[5], array3[5];

    // Initialize arrays
    for (i = 0; i < 5; i++) {
        array1[i] = i;
        array2[i] = i * 3;
    }

    // First loop: perform some operations on array1
    for (j = 0; j < 5; j++) {
        array1[j] += 1;
    }

    // Second loop: perform some operations on array2
    for (k = 0; k < 5; k++) {
        array2[k] += 2;
    }

    // Use the results of the loops
    for (i = 0; i < 5; i++) {
        array3[i] = array1[i] + array2[i];
    }

    // Print the results
    for (i = 0; i < 5; i++) {
        printf("%d ", array3[i]);
    }

    return 0;
}
```

