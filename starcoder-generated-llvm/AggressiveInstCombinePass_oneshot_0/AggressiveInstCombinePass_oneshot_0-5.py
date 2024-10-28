
```cpp
#include <vector>

int func(int x, int y) {
  int result = x - y;
  return result;
}

int main() {
  int result = 0;
  int a = 5;
  int b = 3;
  std::vector<int> vec = {10, 11, 12, 13};
  a = vec[a];
  b = vec[b];
  result = func(a, b);
  short truncated_result = static_cast<short>(result);
  return truncated_result;
}
```

