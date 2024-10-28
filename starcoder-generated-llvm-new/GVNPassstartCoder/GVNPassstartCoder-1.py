
```c
#include <stdio.h>

void example_function() {
    long long a = 10;
    long long b = 20;

    if (a < b) {
        a = a + 1;
    } else {
        a = a - b;
    }

    if (a < b) {
        a = a + 1;
    } else if (b % 2 == 1) {
        a += 1;
    }

    printf("%lld\n", a);
}

int main() {
    example_function();
    return 0;
}
```
