
```cpp
#include <stdio.h>

int x = -20;
int y = 10;
int z = 80;

int main() {
  int main_result = 0;

  // use some variables in a way that does not affect the unused_var
  main_result = y - z;

  printf("%d\n", main_result);

  return main_result;
}
```
