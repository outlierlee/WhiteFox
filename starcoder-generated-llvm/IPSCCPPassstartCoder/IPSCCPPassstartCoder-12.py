```c
#include <stdio.h>

static int global_var = 5;

static int use_global_var() {
  return global_var;
}

int main() {
  int result = 0;
  result = use_global_var();
  printf("result is: %d", result);
  return result;
}
```
