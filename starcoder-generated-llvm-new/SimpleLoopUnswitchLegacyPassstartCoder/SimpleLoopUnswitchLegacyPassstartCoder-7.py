
```c
#include <stdio.h>
#define ITERATION_COUNT (5)

void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        if (flag) {
            printf("Flag is true, iteration %d\n", i);
        } else {
            printf("Flag is false, iteration %d\n", i);
        }
        printf("Flag remains invariant throughout the loop, iteration %d\n", i);
    }
}

int main() {
    int n = ITERATION_COUNT;
    int flag = 0;

    loop_with_condition(n, flag);

    return 0;
}
```

