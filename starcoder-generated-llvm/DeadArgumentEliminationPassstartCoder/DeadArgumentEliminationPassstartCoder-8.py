
```c
#include <stdio.h>

int func_with_unused_params(int a, int b, int c) {
  int result = 10;
  result = a - b * b;
  if (c) result = a / c;
  return result;
}

int main() {
  int x = 16, y = 5, z = 6;
  int my_result = func_with_unused_params((y > 0)?y*10:x, y, z);
  return my_result;
}
```
