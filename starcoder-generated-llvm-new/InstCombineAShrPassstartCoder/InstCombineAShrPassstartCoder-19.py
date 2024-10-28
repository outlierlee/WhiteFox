```c
#include <stdint.h>

int main() {
    int32_t x = 64;
    int32_t y = 10;
    int32_t result;

    result = (x << 16) >> (32 - 24); //(C1 - C2)

    return result;
}
```
