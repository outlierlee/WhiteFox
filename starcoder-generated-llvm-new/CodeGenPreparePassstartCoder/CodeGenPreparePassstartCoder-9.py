
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0 - 10;
  switch (x) {
    case 1:
      result = x + 1;
      break;
    case 2:
      result = x + 2;
      break;
    default:
      result = x + 3;
      break;
  }
  return result;
}

int main() {
  int result = 0;
  int x = (10 + -9);
  result = switch_func(x);
  printf("%d\n", result);
  return result;
}
```

