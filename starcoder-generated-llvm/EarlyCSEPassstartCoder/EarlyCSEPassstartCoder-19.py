
```cpp
#include <iostream>
#include <vector>
#include <string>

static double varargs_func(int x, ...) {
  double result = 10.0;
  if (x % 2) {
    result = x * 2.71828182845904523536; // pi
  } else {
    result = x / 2.71828182845904523536; // pi
  }
  if (x > 100) {
    result = result * 2.0;
  } else {
    result = result * 2.0;
  }
  return result;
}

int main() {
  double result = 0.0;
  int a = (1 << 31);
  std::vector<double> vec = {0.0, 1.0, 2.0, 3.0};
  std::string str = "hello";
  vec.assign(5, 42.0);
  double b = varargs_func(a, 18, 25, vec[1], 1.000000, str[3]);
  result = b;
  std::cout << "Result: " << result << std::endl;
  return 0;
}
```
