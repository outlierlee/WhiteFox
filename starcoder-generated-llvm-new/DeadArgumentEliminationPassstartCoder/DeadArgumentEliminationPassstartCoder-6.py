
```c
#include <stdio.h>
int x = 4;
char y = 'b';
int z = 15;

int func_with_unused_params(int a, int b, int c) {
  int result = 0;
  result = (x % 5);
  return result;
}

int main() {
  int main_result = 0;
  main_result = func_with_unused_params(x, y, z);
  return main_result;
}
```
