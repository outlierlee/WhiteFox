
```cpp
#include <vector>

int func(int x, int y) {
  if (x > y) return x - y;
  else return y - x;
}

int main() {
  int x = (1 << 31);
  int y = ((1 << 31) - 1);
  int result = func(x, y);
  short truncated_result = static_cast<short>(result);
  return truncated_result;
}
```

