
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i, j;

    for (i = 0; i < 100; i += 7) {
        for (j = 0; j < 10; j += 3) {
            sum += i * j;
        }
    }

    printf("Sum: %d\n", sum);
    return sum;
}
```

