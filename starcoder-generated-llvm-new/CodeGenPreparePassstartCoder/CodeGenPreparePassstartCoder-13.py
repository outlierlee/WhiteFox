
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 5:
      result = x * 32 + 15;
      break;
    case 6:
      result = x * 2 - 15;
      break;
    default:
      result = x * 2 - 11;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = (1 << 31);
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```

