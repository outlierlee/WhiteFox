
```cpp
#include <iostream>
#include <vector>
#include <string>

static int varargs_func(int x, ...) {
  int result = 10;
  if (x % 2) {
    result = x * 32 + 15;
  } else {
    result = x - 15;
  }
  if (x > 100) {
    result = result * 2;
  } else {
    result = result * 2;
  }
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 31);
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  for (int i = 0; i < 5; i++) {
    int b = varargs_func(a, 18, 25, vec[1], 1.000000, str[3]);
    if (b > i) {
      result = b;
    } else {
      result = i;
    }
  }
  return result;
}
```
