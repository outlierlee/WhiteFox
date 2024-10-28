
```cpp
#include <stdatomic.h>

int main() {
  // Declare an atomic integer variable
  atomic_int atomic_var = 42;

  // Perform an atomic read-modify-write operation
  // The operation should be idempotent
  atomic_fetch_add(&atomic_var, 0); // Example of an idempotent operation

  return 0;
}
```

