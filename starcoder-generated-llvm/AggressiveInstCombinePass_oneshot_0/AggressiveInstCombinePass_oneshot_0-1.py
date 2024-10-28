
```cpp
#include <vector>
#include <string>

int func(int x, int y) {
  int result = 0;
  if (x % 2) {
    result = x * y + 15;
  } else {
    result = x - y;
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
  int a = (1 << 16);
  int b = (1 << 16);
  int c = func(a, b);
  short truncated_result = static_cast<short>(c);
  result = truncated_result;
  return result;
}
```

