
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<int> vec = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    for (int i = 0; i < 10; ++i) {
        vec[i] = 2 * vec[i] - 1;
        std::cout << vec[i] << "\n";
    }

    for (int i = 9; i != -1; --i) {
        std::cout << vec[i] << "\n";  // Same as earlier, so same optimization possible
    }

    return 0;
}
```

