
```c
#include <stdio.h>

int main() {
    float a = 5.3;
    float b = 7.2;
    float c = 3.5;
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

