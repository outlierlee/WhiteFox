
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int limit = 1000;

    for (int i = 0; i < limit; ++i) {
        sum += i;
    }

    printf("Sum: %d\n", sum);

    return sum;
}
```