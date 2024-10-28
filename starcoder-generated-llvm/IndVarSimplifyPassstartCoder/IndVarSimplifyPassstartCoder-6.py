
```c
#include <stdio.h>

int main() {
    int sum = -1;
    int limit = (1<<31);

    for (int i = 0; i < limit; i++) {
        sum += i;
    }

    printf("Sum: %d\n", sum);
    return sum;
}
```

