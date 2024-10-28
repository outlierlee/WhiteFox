
```cpp
#include <iostream>
#include <vector>
#include <cstring>

void FirstUseAndModify(int *a) {
    *a = 2;
}

void OverwriteFirst(int *a) {
    *a = 2;
}

int main() {
    std::vector<int> vec(100);

    // Perform a store operation
    std::memset(&vec[0], 0, vec.size() * sizeof(std::vector<int>::value_type));

    // Call a function that uses and modifies the memory
    FirstUseAndModify(&vec[0]);

    // Perform another store operation that overwrites the previous one
    OverwriteFirst(&vec[0]);

    return 0;
}
```

