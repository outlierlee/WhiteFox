
```c
#include <stdio.h>

int main() {
    float a = 15.23489;
    float b = 20.54321;
    float c = -34.4355;
    float result;

    if (a < b) {
        result = a;
    } else {
        result = b;
    }

    result = (a > b) ? a : b;

    printf("Result: %f\n", result);

    return 0;
}
```

# C Code ends

