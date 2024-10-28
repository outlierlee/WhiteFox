
```c
#include <stdatomic.h>

int main() {
  atomic_int atomic_var = 42;
  
  int val1 = atomic_load(&atomic_var);
  atomic_fetch_add(&atomic_var, val1);
  return 0;
}
```

