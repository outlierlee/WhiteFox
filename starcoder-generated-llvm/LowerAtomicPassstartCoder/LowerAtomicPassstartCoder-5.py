
```c
#include <stdatomic.h>

atomic_int atomic_var = -200;
int non_atomic_var = 500;

int main() {
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);
  int result = old_value / 2;
  return result;
}
```

