
```c
#include <stdio.h>

float var_args_func(float a, float b, float c) {
    float result;
    if (a > b) {
        if (a > c) {
            result = a;
        } else {
            result = c;
        }
    } else {
        if (b > c) {
            result = b;
        } else {
            result = c;
        }
    }
    return result;
}

int main() {
    float a = 1.5;
    float b = 2.0;
    float c = 0.0000001;
    float out = var_args_func(a + b, a - b, a * b * c);

    printf("Result of func call: %f\n", out);
    return 0;
}
```

