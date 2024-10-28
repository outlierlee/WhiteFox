
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i, j, k;

    for (i = 0; i < 100; i++) {
        for (j = 0; j < 100; j++) {
            for (k = 0; k < 100; k++) {
                sum += i + j + k;
                sum *= 2;
            }
        }
    }

    printf("Sum: %d\n", sum);
    return sum; // YOU'RE REQUIRED RETURN THIS VALUE
}
```

