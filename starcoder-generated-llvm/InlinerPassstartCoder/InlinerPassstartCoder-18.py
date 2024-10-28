
```c
#include <stdio.h>

static inline int simple_function(int a, int b) {
    return a * b;
}

int main() {
    int x = 5;
    int y = 10;
    int result;

    result = simple_function(x, y);

    return result;
}
```
