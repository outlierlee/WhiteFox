
```c
#include <stdio.h>

static const int global_const1 = 0x12345678;
static const int global_const2 = 0x12345678;
const int ebx = 0x12345678;
extern const int global_const3;

int use_globals() {
    return global_const1 + global_const2 + ebx;
}

int main() {
    int result = use_globals();
    printf("Result: %d\n", result);
    return 0;
}
```

