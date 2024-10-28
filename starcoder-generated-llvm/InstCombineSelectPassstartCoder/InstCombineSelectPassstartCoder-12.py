
```c
#include <stdio.h>

int main() {
    float a = 1.0f;
    float b = 2.0f;
    float c = 3.0f;
    float result;

    if (a > b) {
        result = a;
    } else {
        result = b;
    }

    result = (a > b) ? a : b;

    printf("Result: %f\n", result);

    return 0;
}
```

