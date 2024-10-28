
```cpp
#include <iostream>
#include <vector>

int main() {
    int x = -1; // initialize an integer variable
    int y = 0;  // initialize another integer variable

    // A simple conditional structure that creates an unreachable block
    if (x > y) {
        std::cout << "Unreachable block\n";
    } else {
        std::cout << "Reachable block\n";
    }

    // A loop that never executes, creating another unreachable block
    while (x > y) {
        std::cout << "Unreachable loop block\n";
    }

    return 0;
}
```
