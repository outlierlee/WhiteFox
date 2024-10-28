
```c
#include <stdio.h>

static __attribute__((fastcall)) int c_func(int a, int b, int c) {
    printf("Result: %d\n", a * b + c);
    return a * b + c;
}

int main() {
    int result = 0;
    result = c_func(5, 10, 15);
    return result;
}
```

