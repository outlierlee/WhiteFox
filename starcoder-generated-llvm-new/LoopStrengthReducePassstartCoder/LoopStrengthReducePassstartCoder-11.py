
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i;

    // Loop with simple induction variable optimized to reduce branching cost
    for (i = 0; i < 0x7FFFFFFF; i++) {
        sum += i;
        if (sum >= 0x7FFFFFFF) {
            break;
        }
    }

    printf("Sum: %d\n", sum);
    return sum;
}
```
