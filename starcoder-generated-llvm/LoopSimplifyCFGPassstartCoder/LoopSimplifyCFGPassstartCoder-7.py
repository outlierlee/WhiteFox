
```c
#include <stdio.h>

int main() {
    int x = 15;
    int y = 5;
    int result = 0;

    while (x < 30) {
        x = x + y;
        result = x;
    }

    return result;
}
```

The `result` would be 30.