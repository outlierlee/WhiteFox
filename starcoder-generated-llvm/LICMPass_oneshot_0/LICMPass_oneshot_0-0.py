
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
  for (int i = 0; i < 100; ++i) {
    int x = i;
    int b = no_side_effect_func(x);
    if (b > 128 && i % 3 == 0) {
      result = b;
    }
  }
  return result;
}
```
