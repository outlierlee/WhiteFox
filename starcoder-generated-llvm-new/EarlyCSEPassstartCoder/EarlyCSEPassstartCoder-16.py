
```cpp
#include <array>
#include <vector>
#include <algorithm>

int main() {
    std::array<int, 1000> arr = {};
    std::fill(arr.begin(), arr.end(), 5); // Copy 5 million times
    int result = std::accumulate(arr.begin(), arr.end(), 0);
    return result;
}
```

