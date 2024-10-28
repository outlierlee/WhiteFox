
```c
#include <stdio.h>
#define ITERATION_COUNT (1<<15)

int main() {
    int i, j, k;
    int array1[ITERATION_COUNT], array2[ITERATION_COUNT];
    long result = 0;

    // Initialize arrays
    for (i = 0; i < ITERATION_COUNT; i++) {
        array1[i] = i;
        array2[i] = (i*2)-1;
    }

    // The following loops assume they're adjacent
    for (i = 0; i < ITERATION_COUNT; i++) {
        array1[i] += 1;
    }

    for (i = 0; i < ITERATION_COUNT; i++) {
        array2[i] += 2;
    }

    for (i = 0; i < ITERATION_COUNT; i++) {
        result = array1[i] + array2[i];
    }

    printf("%ld", result);

    return 0;
}
```
