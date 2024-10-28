
```cpp
#include <array>
#include <vector>
#include <string>

int main() {
    std::array<std::array<int, 100>, 2> myarray;
    std::vector<std::string> myvector;
    std::string first = "flush", second = "store";

    // Store to different locations within the array
    for (size_t i = 0; i < myarray.size(); ++i) {
        for (size_t j = 0; j < myarray[i].size(); ++j) {
            if (j % 2) myarray[i][j] = myarray[i][j + 1];  // Flush 1 byte side-effect
            else myarray[i][j] = j;  // Store operation
        }
    }

    std::string tmp = first;  // Store operation (this isn't in the pattern)
    first = tmp;  // Flush operation (this isn't in the pattern, however)
    first = second;  // Store operation
    myvector.push_back(first);  // Store operation

    return 0;
}
```

