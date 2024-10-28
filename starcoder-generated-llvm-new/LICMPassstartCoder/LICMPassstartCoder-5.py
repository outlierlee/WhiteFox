
```cpp
#include <iostream>
#include <vector>

int main() {
    int result = 0;
    constexpr int N = 10;
    std::vector<std::vector<int>> array(N, std::vector<int>(N));

    // Initialize the array
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            array[i][j] = i * j;
        }
    }

    // Use accumulate to update result array
    for (int i = 0; i < N; ++i) {
        std::vector<int> v(N);
        result = std::accumulate(array[i].begin(), array[i].end(), result, [](int sum, int x) {
            return x % 2 == 0 ? sum += x : sum;
        });
    }

    std::cout << "Result: " << result << std::endl;
    return result;
}
```

