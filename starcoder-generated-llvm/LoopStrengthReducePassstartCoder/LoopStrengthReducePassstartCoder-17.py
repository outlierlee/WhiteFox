
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i;

    for (i = 0; i < 100; i++) {
        sum += i / 5 + i;
    }

    printf("Sum: %d\n", sum);
    return sum;
}
```

