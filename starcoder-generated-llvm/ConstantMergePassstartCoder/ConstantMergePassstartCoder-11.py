
```c
#include <stdio.h>

static const int global_const = 100;

int use_global() {
  return global_const;
}

int main() {
  int result = use_global() + global_const;
  printf("Result: %d\n", result);
  return 0;
}
```

