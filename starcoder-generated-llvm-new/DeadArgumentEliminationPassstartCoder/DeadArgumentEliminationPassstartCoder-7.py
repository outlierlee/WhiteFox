
```c
#include <stdio.h>

int func_with_unused_params(int a, int b, int c) {
  int result = 0;
  a = 10;
  b = 20;
  result = a + b + c;
  return result;
}

int main() {
  int x = 5;
  int y = 10;
  int z = 15;
  int main_result = 0;
  main_result = func_with_unused_params(x, y, z);
  printf("main_result = %d\n", main_result);
  return 0;
}
```
