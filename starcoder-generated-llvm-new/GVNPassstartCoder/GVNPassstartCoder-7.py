
```c
#include <stdio.h>

void example_function() {
    int a = 10;
    int b = 20;
    if (a < b) {
        a = a + 1;
    } else {
        a = a - 1;
    }
    if (a < b) {
        a = a + 1;
    } else {
        a = a - 1;
    }
    printf("%d\n", a);
}

int main() {
    example_function();
    return 0;
}
```

