
```cpp
#include <iostream>
#include <vector>
#include <memory>

int main() {
    // Allocate memory
    std::unique_ptr<int[]> buffer(new int[100]);
    if (!buffer) return -1;

    // Perform a store operation
    //memset(buffer.get(), 0, 400);
    std::fill_n(buffer.get(), 100, 0);

    // Perform another store operation that overwrites the previous one
    std::fill_n(buffer.get(), 100, 1);

    // Properly deallocate the allocated memory
    buffer.reset();

    return 0;
}
```
