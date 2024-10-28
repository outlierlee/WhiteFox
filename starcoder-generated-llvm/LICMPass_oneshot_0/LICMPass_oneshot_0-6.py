
```cpp
#include <iostream>
#include <vector>
#include <string>

int no_side_effect_func(int x) {
  int result = 0;
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
  for (int i = 0; i < 20; ++i) {
    int x = (1 << 30);
    int a = no_side_effect_func(x);
    if (a < 100) {
      result = 1;
    } else {
      result = 0;
    }
  }
  return result;
}
```
