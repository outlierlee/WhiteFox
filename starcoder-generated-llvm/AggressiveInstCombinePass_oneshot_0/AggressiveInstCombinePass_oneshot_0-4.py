
```cpp
#include <vector>
#include <string>

int func(int a, int b) {
  int result = 0;
  result = a * b + b;
  if (a % 2) {
    result += a + b;
  }
  if (b > 5) {
    result += 5;
  }
  return result;
}

int main() {
  int result = 0;
  int x = (1 << 31);
  int y = (1 << 15);
  result = func(x, y);
  short truncated_result = static_cast<short>(result);
  return truncated_result;
}
```

