
```c
#include <stdio.h>

int x = (1 << 31);
char y = 'A';
char z = 'B';

int main() {
  int main_result = 0;

  int unused_var = x / 1500;

  main_result = (int)y - (int)z;

  printf("%d\n", main_result);

  return main_result;
}
```

