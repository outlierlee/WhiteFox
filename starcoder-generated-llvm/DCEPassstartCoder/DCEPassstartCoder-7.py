
```c
#include <stdio.h>

int x = (1 << 31);
double y = 1.500000;
long long z = 0xFFFFFFAAA112233;

int main() {
  int main_result = 0;

  int unused_var = x * 11;

  main_result = y + z;

  printf("%d\n", main_result);

  return main_result;
}
```

