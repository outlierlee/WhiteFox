
```c
#include <stdint.h>

int main() {
    int32_t x = (1 << 31); 
    int32_t y = -2147483647;
    int32_t result;
    // Left shift with no wrap
    result = (x << 1) >> (31 + 1 - 31);
    return result;
}
```

