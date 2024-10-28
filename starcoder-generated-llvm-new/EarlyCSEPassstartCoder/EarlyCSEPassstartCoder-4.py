
```c
#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int c = 5; // Same value as 'a' to trigger common subexpression elimination

    int result1 = a * b; // First computation
    int result2 = c * b; // Second computation, same as result1

    printf("Result1: %d\n", result1);
    printf("Result2: %d\n", result2);

    return 0;
}
```

