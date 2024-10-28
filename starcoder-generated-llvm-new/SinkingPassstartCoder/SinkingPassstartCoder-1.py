
```c
#include <stdio.h>

int main() {
    int a = 243;
    int b = 7;
    int c; 

    if (a % 2 == 0 && b > 5) {  // Conditional block
        c = a + b;  // Operations inside conditional block
    } else if (a % 2 == 1 && b < 6) {
        c = a - b;  // Operations inside conditional block
    } else {
        c = a * b; // Operations inside conditional block
    }

    printf("%d\n", c); // Use the results in the same conditional block.

    return 0;
}
```
