
```cpp
#include <string>
#include <vector>
#include <sstream>

int func_with_unused_params(int a, int b, int c) {
  int result = 0;
  result = a * b;
  result %= 5;
  return result;
}

int main() {
  int main_result = 0;
  int a[] = {1, 2, 0, 5};
  std::string str = "hello";
  std::vector<std::string> vec(20, str);
  main_result = func_with_unused_params(a[1], vec[2][1], a[0] * a[3] + str.size());
  return main_result;
}
```

