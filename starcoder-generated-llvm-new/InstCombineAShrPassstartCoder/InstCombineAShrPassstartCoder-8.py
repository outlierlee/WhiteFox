
```c
#include <stdint.h>

int main() {
    int32_t x = 92; // Initialize x with any 32-bit integer value
    int32_t y = 81; // Initialize y with any 32-bit integer value
    int32_t result;

    // Perform a left shift with no signed wrap and then an arithmetic right shift
    result = (x << 2) >> 3; // C1 = 2 and C2 = 3

    // Return the result
    return result;
}
```
