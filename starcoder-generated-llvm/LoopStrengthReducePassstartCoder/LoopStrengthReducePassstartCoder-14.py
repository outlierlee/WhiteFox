
```c
#include <stdio.h>

int main() {
    int a = 10;
    int b = 32;
    int sum = 0;

    // loop through a and b to generate a result
    for (int i = 0; i < 10000000; i++) {
        sum += a++ * b;
    }

    printf("Result: %d\n", sum);
    return sum;
}
```
