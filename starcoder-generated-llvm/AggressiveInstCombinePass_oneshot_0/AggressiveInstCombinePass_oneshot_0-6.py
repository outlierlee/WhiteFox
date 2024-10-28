
```cpp
#include <vector>
#include <string>

int func(int x, int y) {
  int result = x * y;
  return result;
}

int main() {
  int x = (1 << 16);
  int y = (1 << 16);
  int result = func(x, y);
  short truncated_result = static_cast<short>(result);
  return truncated_result;
}
```

