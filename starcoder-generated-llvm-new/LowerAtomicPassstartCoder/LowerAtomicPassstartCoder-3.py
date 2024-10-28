
```c
#include <stdatomic.h>

atomic_int atomic_var = 10;
int non_atomic_var = -5;

int main() {
  // perform an atomic read-modify-write operation
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);

  // use the result of the atomic operation
  int result = old_value + non_atomic_var;

  return result;
}
```

