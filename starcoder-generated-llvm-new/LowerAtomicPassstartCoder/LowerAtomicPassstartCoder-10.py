
```c
#include <stdatomic.h>

// declare variables
atomic_int atomic_var = 112;
int non_atomic_var = 45;

int main() {
  // perform an atomic read-modify-write operation
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);

  // use the result of the atomic operation
  int result = old_value * 2;

  return result;
}
```

