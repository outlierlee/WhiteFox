
```c
#include <stdatomic.h>

int main() {
  atomic_int x = ATOMIC_VAR_INIT(0);
  atomic_fetch_add(&x, 1);
  atomic_fetch_add(&x, 1); // Causes an idempotent operation
  return x;
}
```
