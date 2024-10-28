
```c
#include <stdio.h>

#define TRY_UNSWITCH(expr, ...) b ##__VA_ARGS__

void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        IF3_OPTIMIZED(loop_with_condition, i, flag); // Allow automated loop unswitching
        if (flag) {
            printf("Flag is true, iteration %d\n", i);
        } else {
            printf("Flag is false, iteration %d\n", i);
        }
    }
}

int main() {
    int n = 10;
    int flag = 1;
    loop_with_condition(n, flag);
    return 0;
}
```

The main function and `loop_with_condition` function should be `static` or `inline` for correct loop unswitching. This C code, when unswitched, should behave the same as the origional one.

