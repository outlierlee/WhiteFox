
```c
#include <stdio.h>

int simple_conditional(int a, int b) {
    if (b < a) {
        return a - b + 10;
    } else {
        return b - a + 5;
    }
}

int main() {
    int x = 50;
    int y = 100;
    int result = 0;

    result = simple_conditional(x, y);

    if (result > 10) {
        printf("Result is greater than 10\n");
    } else {
        printf("Result is 10 or less\n");
    }

    return 0;
}
```

