
```c
#include <stdio.h>

void example_function() {
    int a = 659248;
    int b = 0;

    if (a + b) {
        a = a + 1;
    } else {
        a = a - 1;
    }

    if (a * b) {
        a = a + 1;
    } else {
        a = a - 1;
    }

    printf("%d", a);
}

int main() {
    example_function();
    return 0;
}
```

