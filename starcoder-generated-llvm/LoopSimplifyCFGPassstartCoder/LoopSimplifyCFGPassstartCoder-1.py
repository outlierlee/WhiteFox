
```c
#include <stdio.h>

int main() {
    int x = 5;
    int y = 1 << x; // if x = 5, y will be 32
    int multiple = 5;
    while (--multiple >= 0) {
        y = y + multiple;
    }
    return y;
}
```

