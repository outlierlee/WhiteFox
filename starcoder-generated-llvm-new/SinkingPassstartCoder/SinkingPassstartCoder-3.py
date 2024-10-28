
```c
#include <stdio.h>

int main() {
    int a = 0xFFFFFFFF;
    int b = 20;
    int c;
    int d = 0x30303030;

    if (a > 5) {
        c = a + b;
    } else {
        c = a - b;
    }

    int result = c * d;

    printf("%d\n", result);

    return result;
}
```

