
```cpp
#include <stdatomic.h>

int main() {
  atomic_int atomic_var = 10;
  int non_atomic_var = 5;
  
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);

  int result = old_value * 42;

  return result;
}
```
