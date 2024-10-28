
```c
#include <stdio.h>

void example_function() {
    int a = 10;
    int b = 20;

    if (a > b) {
        a = a - 2; // Safer to overwrite
    } else {
        a = a + 2; // Safer to overwrite
    }

    if (a > b) {
        a = a - 2; // Safer to overwrite
    } else {
        a = a + 2; // Safer to overwrite
    }

    printf("%d\n", a);
}

int main() {
    example_function();
    return 0;
}
```

