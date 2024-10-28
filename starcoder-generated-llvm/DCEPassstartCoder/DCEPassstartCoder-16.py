
```c
#include <stdio.h>

int x = (1 << 31);
int y = 10000;
int z = 10;

int main() {
  int main_result = 0;

  int unused_var = x - 15;

  main_result = y * z;

  printf("%d\n", main_result);

  return main_result;
}
```

# C Code ends