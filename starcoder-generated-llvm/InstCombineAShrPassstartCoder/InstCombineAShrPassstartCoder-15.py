
```c
#include <stdint.h>

int main() {
    // Declare variables
    int32_t x = -5; // Initialize x with -5
    int32_t y = 2; // Initialize y with 2
    int32_t result;

    // Perform a left shift with no signed wrap and an arithmetic right shift
    result = (x >> 1) >> 1; // Result ≠ 3

    // Return the result
    return result;
}
```

# C++ code ends