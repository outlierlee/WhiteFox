
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 11:
      result = x * 2;
      break;
    case 22:
      if (x > 0) {
        result = x - 1;
      } else {
        result = x + 1;
      }
      break;
    default:
      result = x ^ x;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = 11;
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```

