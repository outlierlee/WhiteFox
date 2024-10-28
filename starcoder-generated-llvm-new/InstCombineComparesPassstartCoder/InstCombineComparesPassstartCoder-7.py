
```cpp
#include <stdio.h>

const int global_array[] = {5, 9, 7, 15, 21};

int main() {
    int result = -1;
    for (int i = 0; i < 5; ++i) {
        if (global_array[i] > 10) {
            result = i;
        }
    }
    return result;
}
```

