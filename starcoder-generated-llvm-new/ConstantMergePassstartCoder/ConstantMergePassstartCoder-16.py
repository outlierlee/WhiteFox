
```c
#include <stdio.h>

static const int global1 = 42;
static const int global2 = 42;
static const int global3 = 42;
static const int global4 = 42;
static const int global5 = 42;
static const int global6 = 42;

int use_globals(int a, int b, int c, int d, int e, int f) {
    return global1 + global2 + global3 + global4 + global5 + global6 + a + b + c + d + e + f;
}

int main() {
    int result = 0;
    for (int i = 0; i<100; i++) {
        result += use_globals(i, i*2, i*3, i*4, i*5, i*6);
    }
    printf("Result: %d\n", result);
    return 0;
}
```

