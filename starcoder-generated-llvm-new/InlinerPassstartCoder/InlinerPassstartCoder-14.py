
```c
#include <stdio.h>

static inline int simple_function(int a, int b) {
    return a - b;
}

int main() {
    int x = 1000;
    int y = 996;
    int result;

    result = simple_function(x, y);

    printf("The result is: %d\n", result);

    return result;
}
```
