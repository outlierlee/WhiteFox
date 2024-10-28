
```cpp
#include <iostream>
#include <random>

int main() {
    int x = rand(); // initialize x 
    int y = rand(); // initialize y
    int z = x + y; // perform operation
    if (z == x + y) { // perform comparison
        std::cout << "The evaluation yields true" << std::endl;
    }
    return 0;
}
```
