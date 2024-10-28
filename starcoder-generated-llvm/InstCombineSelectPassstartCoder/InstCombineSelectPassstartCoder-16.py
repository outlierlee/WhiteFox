
```cpp
#include <stdio.h>

int main() {
    float a = 4.5f;
    float b = 1.2345678f;
    float c = 951.62331f;
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

