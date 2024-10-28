
```cpp
#include <atomic>

int main() {
  std::atomic_int atomic_var = 10;
  atomic_var.fetch_add(0, std::memory_order_relaxed);

  return 0;
}
```

