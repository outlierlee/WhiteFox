
```c
#include <stdio.h>

static inline int simple_func(int a, int b) {
    a = a + 5;
    b = b * a;
    a = b / a;
    return a + b;
}

int main() {
    int x = 5;
    int y = 10;
    int result;
    result = simple_func(x, y);
    return result;
}
```
