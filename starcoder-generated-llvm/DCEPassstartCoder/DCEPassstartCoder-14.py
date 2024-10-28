
```c
#include <stdio.h>

int main() {
  int main_result = 0;
  int x = 1 * 2 % 3;
  int y = 3 * 2 / 1;
  int z = 7 * 2 + 1;
  int unused_var = x + y;
  main_result = x * z;

  printf("%d\n", main_result);

  return main_result;
}
```

