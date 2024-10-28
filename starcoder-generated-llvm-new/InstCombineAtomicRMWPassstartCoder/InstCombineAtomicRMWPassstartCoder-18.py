
```cpp
#include<stdatomic.h>

int main() {
  atomic_int var = ATOMIC_VAR_INIT(42);

  atomic_fetch_add(&var, 0);
  atomic_fetch_sub(&var, 0);
  atomic_fetch_or(&var, 0);

  return 0;
}
```

