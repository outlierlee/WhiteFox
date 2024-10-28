
```c
#include <stdint.h>

static int32_t global_var = 6;

static int32_t use_global_var() {
  return global_var;
}

int main() {
  int32_t result = 0;
  result = use_global_var();
  return result;
}
```
