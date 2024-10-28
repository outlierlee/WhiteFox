
```c
#include <stdio.h>

int main() {
    int a = (1 << 11);
    int b = (1 << 14);
    int c = a << 2;
    int d = ((a << 3) << 3) + (b << 1); // Common expression "c << 3"
    int result1 = c | d | 10; // First computation
    int result2 = (a << 2) | (b << 2) | 5; // Second computation, due to duplication with result1
    printf("Result1: %d\n", result1);
    printf("Result2: %d\n", result2);
    return 0;
}
```

