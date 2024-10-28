
```cpp
#include <stdatomic.h>

int main() {
  // declare variables
  atomic_int atomic_var = (1<<19);
  int non_atomic_var = 1<<13;

  // perform an atomic read-modify-write operation
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);

  // use the result of the atomic operation
  int result = 211 * old_value; // multiply old_value by 211

  return result; // return the result
}
```
