
```c
#include <stdatomic.h>

static atomic_int atomic_var = 15;
static int non_atomic_var = 5;

int main() {
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);
  int result = old_value + 10;
  return result;
}
```

