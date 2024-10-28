
```c
#include <stdatomic.h>

int main() {
  atomic_int atomic_var = 15;
  atomic_fetch_add(&atomic_var, 15);
  return 0;
}
```

