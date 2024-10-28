
```cpp
#include <stdatomic.h>

atomic_int atomic_var = (1 << 31);
int non_atomic_var = 5;

int main() {
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);
  int result = old_value * 3;
  return result;
}
```

