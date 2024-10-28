
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    int x = (1 << 7) + (1 << 6);
    int y = (1 << 5) + (1 << 4);
    int z = x + y;
    if (z == x + y) {
        std::cout << "The condition is true." << std::endl;
    }
    return z;
}
```

