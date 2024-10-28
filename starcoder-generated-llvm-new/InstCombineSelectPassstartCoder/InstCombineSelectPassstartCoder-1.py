
```cpp
#include <iostream>

int main() {
    float a = 10.2f;
    float b = 5.6f;
    float c = -3.4f;
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

