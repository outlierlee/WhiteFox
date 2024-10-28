
```cpp
#include <vector>
#include <string>

void __attribute__((noinline)) func(int a, double b, const std::vector<int>& vec, const std::string& str) {
  a += 5;
  b += 3.5;
  vec[0] = 10;
  str = "";
}

int main() {
  int a = 5;
  double b = 3.0;
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";

  func(a, b, vec, str); 

  return 0;
}
```

