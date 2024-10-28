
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  if (x == 0) {
    result = x * (x + 1);
  } else if (x == 1) {
    result = x * (x + 2);
  } else {
    result = x * (x * 3);
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = 3;
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```
