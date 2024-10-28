
```c
#include <stdio.h>

static const int global_const1 = 42;
static const int global_const2 = global_const1;

int use_globals() {
    return global_const1 + global_const2;
}

int main() {
    int result = use_globals();
    printf("Result: %d\n", result);
    return 0;
}
```

