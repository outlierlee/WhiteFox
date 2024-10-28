
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int limit = 1000000;
    for (int i = 0; i < limit; i++) {
        int mult = 1;
        if (i % 2) {
            mult = i * 16;
        } else {
            mult = i - 15;
        }
        if (i > 100) {
            mult = mult * 2;
        } else {
            mult = mult * 3;
        }
        sum += mult;
    }
    printf("Sum: %d\n", sum);
    return 0;
}
```
