
```cpp
#include <stdatomic.h>

atomic_int atomic_var{42};
int non_atomic_var{-1};

int main() {
  int old_value = atomic_fetch_sub(&atomic_var, non_atomic_var);
  int result = old_value - 10;
  return result;
}
```

