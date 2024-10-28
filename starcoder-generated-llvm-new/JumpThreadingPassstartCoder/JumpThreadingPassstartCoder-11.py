
```cpp
#include <iostream>
#include <vector>

int varargs_func(int x, ...) {
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
  vec.assign(5, 42);
  result = varargs_func(a, 18, 25, vec[1]);
  if (result > 1000) {
    std::cout << "Result is greater than 1000" << std::endl;
  } else {
    std::cout << "Result is 1000 or less" << std::endl;
  }
  return 0;
}
```

