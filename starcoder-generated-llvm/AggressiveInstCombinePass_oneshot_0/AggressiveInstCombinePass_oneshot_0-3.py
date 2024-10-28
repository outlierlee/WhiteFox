
```cpp
#include <vector>
#include <string>

int func(int x, int y) {
  int result = 0;
  if (y == 0) {
    result = 42;
  } else {
    result = x / y;
  }
  return result;
}

int main() {
  int result = 0;
  int x = (1 << 31);
  int y = 0;
  result = func(x, y);
  return static_cast<short>(result);
}
```

