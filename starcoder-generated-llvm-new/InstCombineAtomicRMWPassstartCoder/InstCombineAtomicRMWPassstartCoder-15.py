
```c
#include <stdatomic.h>

int main() {
  atomic_int atomic_var = 5;
  atomic_fetch_add(&atomic_var, 0); // idempotent operation
  return 0;
}
```
