
```cpp
#include <stdio.h>

int main() {
    float a = 2.5;
    float b = 3.14159;
    float c = 1.618;
    float result;

    if (a > b) {
        result = a + c;
    } else {
        result = b - c;
    }

    result = (a > b) ? a + c : b - c;

    printf("Result: %f\n", result);

    return 0;
}
```

