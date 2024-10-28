
```cpp
#include <vector>
#include <string>

int main() {
  int x = (1 << 31);
  int y = 40;
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  if (x < y) {
    x -= 5;
    y += 2;
    vec[0] = str[x];
  }
  return 0;
}
```
# C++ Code Ends

