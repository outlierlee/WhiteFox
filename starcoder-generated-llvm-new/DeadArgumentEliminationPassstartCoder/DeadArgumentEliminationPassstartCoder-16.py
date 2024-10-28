
```cpp
#include <vector>
#include <string>
#include <float.h>

int func_with_unused_params(int a, int b, int c) {
  int result = 10;
  result = a * 4 + 15;
  return result;
}

int main() {
  int main_result = 0;
  int x = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  main_result = func_with_unused_params(x, vec[1], x ^ vec[2]);
  return main_result;
}
```