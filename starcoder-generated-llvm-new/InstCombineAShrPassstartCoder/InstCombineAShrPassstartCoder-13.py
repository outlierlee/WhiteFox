
```c
#include <stdint.h>

int main() {
    // initializing constants
    int32_t C1 = 5;
    int32_t C2 = 2;

    // Declare variables
    int32_t x = 500;
    int32_t y = 200;
    int32_t result;

    // Perform a left shift with no signed wrap and then an arithmetic right shift
    result = (x << C1) >> C2; 

    // Return the result
    return result;
}
```

