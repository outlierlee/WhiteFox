
```c
#include <stdint.h>

int main() {
    int32_t x = 20;
    int32_t y = 20;
    int32_t result;

    // Perform a left shift with no signed wrap and then an arithmetic right shift
    result = (x <<12) >>4;

    // Return the result
    return result;
}
```

