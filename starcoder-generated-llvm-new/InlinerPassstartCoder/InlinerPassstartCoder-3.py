
```c
#include <stdio.h>

static inline int simple_function(int a, int b) {
    return a * b; // Simple operation that can be easily inlined
}

int main() {
    int x = 10;
    int y = 5;
    int result = 0;

    result = simple_function(x, y);

    return result;
}
```

