
```c
#include <stdio.h>

static const int global_const = 42;
static const int same_const = 42;
static const __attribute__((weak)) int weak_const = 16;
static const int non_const = 36;

int use_globals() {
    return global_const + non_const;
}

int main() {
    int result = use_globals();
    printf("Result: %d\n", result);
    return 0;
}
```

