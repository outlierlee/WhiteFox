
```cpp
#include <vector>
#include <string>

int main() {
  int x = -123;
  int y = 0;
  std::vector<int> vec = {0, 1, 2, 3};
  while (!vec.empty() && x != vec[0]) {
    vec.erase(vec.begin());
  }
  return 0;
}
```
