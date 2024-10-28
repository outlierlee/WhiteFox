
```cpp
#include <vector>
#include <string>

static int varargs_func(int x, ...) {
  int result;
  if (x % 2) {
    result = x;
  } else {
    result = 2 * x;
  }
  if (x > 100) {
    result = result * 2;
  } else {
    result = result * 2;
  }
  return result;
}

int main() {
  int a = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  int b = varargs_func(a, 18, 25, vec[1], 1.000000, str[3]);
  return b;
}
```
