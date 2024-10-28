
```c
#include <stdio.h>

int simple_conditional(int a, int b, int c) {
    if (a > b) {
        return c;
    } else {
        return a + b;
    }
}

int main() {
    int x = 1302;
    int y = 3553;
    int z = 59;
    int result = 0;

    result = simple_conditional(x, y, z);

    if (result > 10000) {
        printf("Result is greater than 10000\n");
    } else {
        printf("Result is less than or equal to 10000\n");
    }

    return 0;
}
```

