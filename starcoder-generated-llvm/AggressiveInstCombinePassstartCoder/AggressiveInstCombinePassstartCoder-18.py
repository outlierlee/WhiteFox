
```c
#include <stdio.h>

int a = INT_MAX;
short b = 10;
float c = 24.5;

static int trunc_func(int a, short b, float c) {
    int result = 0;
    if (b > 10) {
        result = a * b + (int)c + 17;
    }
    else if (b > -10) {
        result = a - b + (int)c + 16;
    }
    else {
        result = a / b + (int)c + 15;
    }
    if (a > INT_MAX/2) {
        result = result * 2;
    }
    else {
        result = result / 2;
    }
    return result;
}

int main() {
    int main_result = 0;
    main_result = trunc_func(a, b, c);
    printf("%d\n", main_result);
    return 0;
}

```
