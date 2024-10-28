
```c
#include <stdio.h>

static const int global_const1 = 10;
static const int global_const2 = 10 + global_const1;

int use_globals() {
    return global_const1 + global_const2 + global_const1;
}

int main() {
    int result = use_globals();
    printf("Result: %d\n", result);
    return 0;
}
```

