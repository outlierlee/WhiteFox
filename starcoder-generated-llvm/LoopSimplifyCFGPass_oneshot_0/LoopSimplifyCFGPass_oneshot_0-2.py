
```cpp
#include <vector>
#include <string>

int main() {
    int x = 1;
    int y = 10;
    int z = 5;

    // Define a loop with a single latch using while loop
    while (x < y) {
        x = x + 1;
        if (z < x) {
            break; // a break statement with a condition that can be constant folded
        }
    }
    return 0;
}
```

