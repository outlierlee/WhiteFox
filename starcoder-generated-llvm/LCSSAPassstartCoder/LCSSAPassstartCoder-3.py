
```c
#include <stdio.h>

int main() {
    int result = 0;

    int a = 10, b = 20, c = 30;

    for (int i = 0; i < c; i++) {
        if (a > b) {
            result += i;
        } else {
            result += c;
        }
    }

    if (result > a) {
        printf("Result is greater than a\n");
    } else {
        printf("Result is less than or equal to a\n");
    }

    return 0;
}
```

