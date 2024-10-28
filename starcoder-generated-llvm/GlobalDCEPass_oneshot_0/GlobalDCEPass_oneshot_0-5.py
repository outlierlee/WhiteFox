
```cpp
#include <vector>
#include <string>

void unused_func() {
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  str.insert(str.size(), " world");
}

int main() {
  int a = (1 << 31);
  unused_func();
  return (a > 20) ? a : 0;
}
```
