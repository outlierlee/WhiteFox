
```cpp
#include <stdio.h>

// Define two arrays and a constant
const int SIZE = 10;
int arr1[SIZE] = {0};
int arr2[SIZE] = {0};

// Define a function that has a long cycle
void long_cycle_function() {
    for (int i = 0; i < SIZE; i++) {
        arr1[i] = i * 2;
    }
    for (int i = 0; i < SIZE; i++) {
        arr2[i] = arr1[i] * 2;
    }
    for (int i = 0; i < SIZE; i++) {
        arr1[i] = arr2[i] + i;
    }
}

int main() {
    long_cycle_function(); // Call the function
    // Print the array to prevent dead code elimination
    for (int i = 0; i < SIZE; i++) {
        printf("%d ", arr1[i]);
    }
    return 0;
}
```

