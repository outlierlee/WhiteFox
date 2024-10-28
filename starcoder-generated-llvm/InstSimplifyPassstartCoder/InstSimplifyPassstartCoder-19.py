
```cpp
#include <iostream>
#include <vector>
#include <string>

static double varargs_func(int x, ...) {
  double result = 10.0;
  if (x % 2) {
    result = x * 2.71828;
  } else {
    result = x + 10.0;
  }
  if (x > 100) {
    result = result / 1.41421;
  } else {
    result = result * 1.818;
  }
  return result;
}

int main() {
  double result = 0.0;
  int a = 20;
  double b = 0.0;
  std::vector<double> vec = {3.14159, 2.71828, 1.61803, 1.41421};
  std::string str = "hello";
  vec.assign(5, 42.0);
  result = varargs_func(a, 22.5, vec[1], cos(0.785), exp(-4.5));
  printf("result = %.2f\n", result);
  return 0;
}
```

