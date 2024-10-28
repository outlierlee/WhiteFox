
```c
#include <stdatomic.h>

#define OPERATOR +

atomic_int atomic_var = 10;
int non_atomic_var = 5;

int main() {
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);
  int result = old_value OPERATOR 5;
  return result;
}
```

