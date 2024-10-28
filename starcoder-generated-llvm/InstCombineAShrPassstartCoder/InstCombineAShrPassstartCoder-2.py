
```cpp
#include <stdint.h>

int main() {
    int32_t x = (1 << 13);
    int32_t y = (1 << 12);
    int32_t result;

    result = (x << 14) >> (12);

    return result;
}
```

