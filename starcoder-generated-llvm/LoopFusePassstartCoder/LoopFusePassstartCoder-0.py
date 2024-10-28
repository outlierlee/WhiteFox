
```cpp
#include <vector>
#include <numeric>
#include <iostream>

int main() {
  std::vector<int> array1(10), array2(10), array3(10);
  std::iota(array1.begin(), array1.end(), 0);
  std::iota(array2.begin(), array2.end(), 0);
  std::transform(array1.begin(), array1.end(), array1.begin(), [](int x) { return x + 1; });
  std::transform(array2.begin(), array2.end(), array2.begin(), [](int x) { return x + 2; });
  std::transform(array1.begin(), array1.end(), array2.begin(), array3.begin(), std::plus<int>());

  for (const auto& x : array3) {
    std::cout << x << " ";
  }
  return 0;
}
```
