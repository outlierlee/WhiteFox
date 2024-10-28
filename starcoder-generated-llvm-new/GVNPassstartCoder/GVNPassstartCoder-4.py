
```cpp
#include <stdio.h>

void example_function() {
    int a = 10;
    int b = 20;

    if (a < 2 * b) {
        a = a;
    } else {
        a = a / 2;
    }

    if (a > 2 * b) {
        a = a + 10;
    } else {
        a = a - 10;
    }

    printf("%d\n", a);
}

int main() {
    example_function();
    return 0;
}
```
