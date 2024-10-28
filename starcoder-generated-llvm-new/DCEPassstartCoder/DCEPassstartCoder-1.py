
```c
#include <stdio.h>

int x = 5;
int y = 20;
int z = 10;

int main() {
  int result = 0;
  int unused_var = x / 2; // this is only assigned to, but never used.
  result = y * z;
  printf("%d\n", result);
  return result;
}
```
# C Code ends