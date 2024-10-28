
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  switch(x) {
    case 1:
      result = (x << 31);
      break;
    case 2:
      result = 1000000 * x;
      break;
    default:
      result = x / 2;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = 42;
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```

This C++ program demonstrates a version of the requirement rule, where the `switch_func` function implements a similar pattern, but is more comple with better use of function and operator characteristic.

