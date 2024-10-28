
```c
#include <stdint.h>

int main() {
    // Declare variables
    int32_t x = -1;
    int32_t y = 0;
    int32_t result;

    // Perform a left shift with no signed wrap and then an arithmetic right shift
    result = (x <<10) >>5;

    // Return the result
    return result;
}
```

