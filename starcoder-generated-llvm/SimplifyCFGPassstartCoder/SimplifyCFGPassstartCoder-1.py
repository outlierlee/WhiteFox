```cpp
#include <stdio.h>

int main() {
    int x = 1; // declare and initialize a variable
    int y = -1; // declare and initialize another variable

    int result = 0;

    // A simple conditional structure that creates an unreachable block
    if (x > y) {
        // This block is unreachable because x is not greater than y
        result = 2;
    } else {
        // This block is reachable
        result = 1;
    }

    // A loop that never executes, creating another unreachable block
    while (x > y) {
        result += 1;
    }

    // A loop that executes, creating another reachable block
    for (int i = 0; i < 10; ++i) {
        result -= 1;
    }

    return result;
}
```
