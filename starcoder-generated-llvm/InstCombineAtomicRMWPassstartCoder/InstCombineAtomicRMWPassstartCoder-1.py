
```cpp
#include <atomic>

int main() {
  // Define an atomic integer variable
  std::atomic<int> atomic_var = stdatomic_const_init(0);

  // Perform an atomic read-modify-write operation
  // The operation should be idempotent and not 'Or'
  atomic_fetch_add(&atomic_var, 0); // Example of an idempotent operation

  return 0;
}
```

