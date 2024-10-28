
```c
#include <stdint.h>

int main() {
    int32_t x = 21;
    int32_t y = 1 << 30;
    int32_t result;

    // Perform a left shift with no signed wrap and then an arithmetic right shift
    result = (x <<31) >>3;

    return result;
}
```

