
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 1:
      result = x + 1;
      break;
    case 2:
      result = x + 2;
      break;
    case 63:
      result = x % 3;
      break;
    default:
      result = x + 3;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = sizeof(int);
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```
