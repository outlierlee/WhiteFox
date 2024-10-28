
```cpp
#include <iostream>
#include <vector>

int main() {
    int size = 100;
    std::vector<int> buffer(size);
    for (int i=0; i<size; i++) {
        buffer[i] = 1;
    }
    for (int i=0; i<size; i++) {
        buffer[i] = 2;
    }
    return 0;
}
```

