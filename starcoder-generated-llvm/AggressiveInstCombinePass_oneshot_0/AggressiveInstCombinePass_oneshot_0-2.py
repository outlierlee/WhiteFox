
```cpp
#include <vector>
#include <string>

int func(int x, int y) {
  int result = x + y;
  if (x < 100 || y < 100) {
    result += y;
  } else {
    result += x;
  }
  if (x > 1000 || y > 1000) {
    result *= 2;
  } else {
    result *= 3;
  }
  return result;
}


int main() {
  int x = (1 << 31) + 1000;
  int y = (1 << 31) + 2000;
  int result = func(x, y);
  short truncated_result = static_cast<short>(result);
  return truncated_result;
}
```

