
```c
#include <stdio.h>

#define N 100000000

int main() {
    int sum = 0;
    register int i;

    for (i = 0; i < N; i++) {
        sum += i;
    }
    printf("Sum: %d\n", sum);
    return sum;
}
```

