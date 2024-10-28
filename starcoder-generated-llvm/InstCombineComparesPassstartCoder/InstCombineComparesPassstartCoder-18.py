
```cpp
#include <stdio.h>

static const int global_array[] = {-3, 5, 12, 19, 25, 32};

int main() {
    int result = 0;
    for (int i = 0; i < sizeof(global_array) / sizeof(int); ++i) {
        if (global_array[i] % 3 == 0) {
            result = i;
        }
    }
    return result;
}
```

