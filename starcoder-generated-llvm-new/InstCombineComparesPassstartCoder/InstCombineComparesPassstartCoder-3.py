
```c
#include <stdio.h>

const int global_array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
const int target_index = 5;

int main() {
    int result = 0;
    int found_index = 0;
    for (int i = 0; i < sizeof(global_array) / sizeof(global_array[0]); ++i) {
        if (global_array[i] == target_index) {
            found_index = i;
            break;
        }
    }
    result = found_index;
    return result;
}
```

