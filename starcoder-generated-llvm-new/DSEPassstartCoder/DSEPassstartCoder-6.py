
```cpp
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<int> vec = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    for (int i = 0; i < 10; ++i) {
        vec[i] = 0;
    }
    for (int j = 0; j < 10; ++j) {
        vec[j] = 1;
    }
    vec.clear();
    return 0;
}
```

