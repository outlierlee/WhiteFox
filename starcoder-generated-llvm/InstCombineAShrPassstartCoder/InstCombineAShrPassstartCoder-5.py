
```cpp
#include <stdint.h>

int main() {
    int32_t x = -16;
    int32_t y = -256;
    int32_t result;

    result = (x << (31)) >> (31 - 16);

    return result;
}
``` 
