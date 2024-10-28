
```cpp
#include <vector>
#include <string>

int no_side_effect_func(int x) {
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
  int b = 0;
  for (auto i = 0; i < 100; ++i) {
    b = no_side_effect_func(a);
    if ((b - 1) % 2 == 0) {
      vec.assign(5, 42);
      str[2] = 'W';
    }
    a += b;
    result = a;
  }
  return result;
}
```
