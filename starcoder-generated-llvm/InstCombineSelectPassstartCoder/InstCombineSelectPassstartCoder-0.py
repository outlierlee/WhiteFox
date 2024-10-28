
```cpp
#include <stdio.h>

int main() {
    float a = 12345678.0f;
    float b = 98765432.12345678f;
    float c = -98765432.12345678f;
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
