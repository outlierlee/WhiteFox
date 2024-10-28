
```c
#include <stdio.h>

int main() {
    int sum = 0;
    int i;
    int t = 100000000;
    for (i = 0; i < 5000; i++) {
        sum += 5000;
    }

    for (i = 0; i < 5000; i++) {
        sum -= 5000 * t;
        sum = sum < 0 ? -sum : sum;
    }
    printf("Sum: %d\n", sum);
    return sum;
}
```

