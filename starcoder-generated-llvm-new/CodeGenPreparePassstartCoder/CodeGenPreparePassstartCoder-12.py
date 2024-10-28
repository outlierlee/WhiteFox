
```c
#include <stdio.h>

int switch_func(int x) {
  int result;
  switch (x) {
    case 1:
      result = x * 5;
      break;
    case 2:
      result = x * 4;
      break;
    default:
      result = x * 2;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = 1000;
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```

