
```c++
#include <iostream>

inline int inline_func(int a, int b) {
  return a + b;
}

int main() {
  int result = 0;
  int x = 5;
  int y = 10;
  result = inline_func(x, y);
  return result;
}
```

