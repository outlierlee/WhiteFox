
```cpp
#include <stdio.h>

int main() {
    int result = 0;  // declare the result
    int i, j;  // loop variables
    int array[10][10];  // declare a 2D array

    // Initialize the array with some values
    for (i = 0; i < 10; ++i) {
        for (j = 0; j < 10; ++j) {
            array[i][j] = i * j;  // some computation
        }
    }

    // Outer loop
    for (i = 0; i < 10; ++i) {
        // Inner loop
        for (j = 0; j < 10; ++j) {
            // Perform some computation that involves a condition
            if (array[i][j] % 2 == 0) {
                result += array[i][j];  // accumulate result
            }
        }
    }

    // Return the result
    return result;
}
```

# C code ends