
```c
#include <stdint.h>

#define C1 15U
#define C2 3U

int main() {
    int32_t x = 10;
    int32_t y = 7;
    int32_t result;
    
    result = (x << C1) >> C2;
    
    return result;
}
```

