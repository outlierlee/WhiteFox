
```cpp
#include <stdint.h>

int main() {
    int32_t x = (1 << 31); // This number is all 1s in binary in 32 bits, equivalent to 2147483647 and also equivalent to -2147483648 due to representation of negative numbers
    int32_t y = (1 << 30);
    int32_t result;

    // Initiate the transformation: (X <<nsw 1) >>s 2 --> X <<nsw 1 - 2 --> X <<nsw 1
    result = (x << 1) >> 2;

    return result;
}
```

