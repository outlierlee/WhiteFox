
```c
#include <stdio.h>

int main() {
  unsigned a = (1 << 31);
  int x = (int) (a*1.0);
  printf("%d\n", x);
  return 0;
}
```
