
```c
#include <stdio.h>

int x = -100000;
int y = 20;
int z = 30;

int main() {
  int main_result = 0;

  int unused_var = x + y;

  printf("%d\n", unused_var);

  main_result = y * z;

  printf("%d\n", main_result);

  return main_result;
}
```

