
```c
#include <stdio.h>

// Result of fused loop optimization
static int optimized_result();

int main() {
    int i, j, k;
    int array1[100], array2[100], array3[100], array4[100];

    // Initialize arrays
    for (i = 0; i < 100; i++) {
        array1[i] = i * 2;
        array2[i] = i + 1;
        array3[i] = i * 3;
        array4[i] = i * 4;
    }

    // Fused loop to perform multiple operations on array2 and array3
    for (k = 0; k < 100; k++) {
        array2[k] += array3[k];
        array1[k] += array4[k];
    }

    // Print the results and return the result
    for (i = 0; i < 100; i++) {
        printf("%d %d\n", array1[i], array2[i]);
    }
    printf("Optimized result: %d\n", optimized_result());

    return 0;
}

static int optimized_result() {
    // Assuming some optimization is placed here...
    return 42;
}
```

