
```c
#include <stdio.h>

static const int global_const1 = (1 << 24);

static int use_globals() {
    return global_const1 + global_const1;
}

int main() {
    int result = use_globals();
    printf("Result: %d\n", result);
    return 0;
}
```
