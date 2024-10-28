
```c
#include <stdio.h>

static inline int simple_function(char *a, int b, float c) {
    return (int)(a[0]*b + c);
}

int main() {
    char str[] = "Hello_World"; int y = 42; float z = 15.32;
    int result;
    result = simple_function(str, y, z);
    printf("The result is: %d\n", result);
    return result;
}
```

