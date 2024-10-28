
```c
#include <stdio.h>

int main() {
    int a = 1 << 31;
    int b = a + 1;
    int c, d;

    if (a > 0) {
        c = a + b;
    } else {
        c = a - b;
    }
    d = c * 2;

    printf("%d\n", d);

    return 0;
}
```
