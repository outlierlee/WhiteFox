
```cpp
#include <iostream>
#include <vector>

static int trunc_func(int a, int b, int c, int d) {
  int result = 0;
  result = (a + d) / (b * c);
  return result;
}

int main() {
  float result = 0;
  int a = (1 << 31); // 2^31
  int b = (1 << 30); // 2^30
  int c = 256 * 1024;
  int d = 21;
  int main_result = trunc_func(a, b, c, d);
  result = main_result + 0.6f;
  std::cout << result << std::endl;
  return 0;
}
```

