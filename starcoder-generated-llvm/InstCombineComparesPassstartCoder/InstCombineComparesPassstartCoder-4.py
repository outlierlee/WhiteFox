
```cpp
#include <stdio.h>

const int global_array[] = {1, 2, 3, 4, 5};

int main() {
    int result = 0;
    for (int i = 0; i < 5; ++i) {
        if (global_array[i] != (i + 1)) {
            result = -1;
            break;
        }
        result = i;
    }
    return result;
}
```

