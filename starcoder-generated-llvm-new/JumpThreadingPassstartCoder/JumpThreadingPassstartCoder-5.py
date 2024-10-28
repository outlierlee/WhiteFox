
```c
#include <stdio.h>

int simple_conditional(int a, int b) {
    return a * 10 + b * 2;
}

int main() {
    int a = 3;
    int b = 5;
    int result = 0;

    // Use a constant expression in the function call
    result = simple_conditional(3, 6);

    // Use the result with a different constant expression
    if (result < 50) {
        printf("Result is smaller than 50\n");
    } else {
        printf("Result is 50 or larger\n");
    }

    return 0;
}
```

