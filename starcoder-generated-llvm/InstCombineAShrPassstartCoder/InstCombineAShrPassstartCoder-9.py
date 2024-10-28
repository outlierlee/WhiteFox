
```c
#include <stdint.h>

int main() {
    int32_t x = (1 << 31);
    int32_t y = -1;
    int32_t result = (x << 11) >>10;
    return result;
}
```
