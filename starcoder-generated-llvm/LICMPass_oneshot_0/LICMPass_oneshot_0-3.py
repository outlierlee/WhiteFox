
```cpp
#include <vector>
#include <string>

int no_side_effect_func(int x) {
  int result = 0;
  if (x % 2) {
    result = x * 32 + 15;
  }
  else {
    result = x - 15;
  }
  if (x > 100) {
    result = result * 2;
  }
  else {
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
  for (int i = 0; i < 10; ++i) {
    int b = no_side_effect_func(a + 5*i);
    if (b > a) {
      result = b;
    }
  }
  return result;
}
```
