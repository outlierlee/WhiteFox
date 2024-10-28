
```c
#include <stdio.h>
#include <stdlib.h>

int func_with_unused_params(int a, int b, int c) {
  int result = rand() % 100;
  return result;
}

int main() {
  int x = 17;
  int y = 52;
  int z = 7;
  int main_result = func_with_unused_params(x, y, z);
  return main_result;
}
```

