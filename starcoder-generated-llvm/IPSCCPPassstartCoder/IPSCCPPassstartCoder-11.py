
```c
#include <string.h>

static int global_var = 'S';

static int use_global_var() {
  return global_var;
}

int main() {
  int result = 0;
  result = use_global_var();
  return result;
}
```

