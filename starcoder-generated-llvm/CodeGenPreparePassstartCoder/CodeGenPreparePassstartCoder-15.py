
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  if (x == 1) {
    result = x;
  } else if (x == 2) {
    result = x;
  } else {
    result = x * 2;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = 1;
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```
