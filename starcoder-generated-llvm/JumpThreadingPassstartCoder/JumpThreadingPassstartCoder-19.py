
```cpp
#include <iostream>
#include <vector>
#include <string>

static int varargs_func(int x, ...) {
  int result = 10;
  if (x == 1) {
    result = x * 32 + 15;
  } else if (x < 0) {
    result = x - 15;
  }
  return result;
}

int main() {
  int result = 0;
  int a = 1;
  std::vector<int> vec = {0, 1, 2, 3, 4};
  std::string str = "hello";
  int index = 0;
  int b = varargs_func(a, str[index]);
  result = b;
  return result;
}
```

