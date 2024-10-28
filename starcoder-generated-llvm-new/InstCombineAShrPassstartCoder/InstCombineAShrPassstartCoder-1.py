
```c
#include <stdint.h>

int main() {
    // Declare variables
    int32_t x = 250;
    int32_t y = -1;
    int32_t result;

    // Perform a left shift with no signed wrap and then an arithmetic right shift
    result = (x << (21) >> (7));

    // Return the result
    return result;
}
```
