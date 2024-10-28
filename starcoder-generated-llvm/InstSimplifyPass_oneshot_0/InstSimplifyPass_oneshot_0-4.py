
```cpp
#include <vector>
#include <string>

int main() {
    int x = (1 << 31) - 1; // declare variable x
    int y = (1 << 31); // declare variable y
    int z = x + y; // perform some operation
    if (z == x + y) { // compare the result with the same operation
        // do something
    }
    return z;
}
```
