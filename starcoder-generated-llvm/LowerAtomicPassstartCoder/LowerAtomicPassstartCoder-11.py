
```cpp
#include <atomic>

int main() {
  std::atomic_int atomic_var = 10;
  int non_atomic_var = 5;

  int old_value = atomic_var.fetch_add(non_atomic_var, std::memory_order_seq_cst);
  int result = old_value + non_atomic_var;

  return result;
}
```
