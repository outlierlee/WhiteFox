
```cpp
#include <atomic>

std::atomic <int> atomic_var = {100};
int non_atomic_var = {50};

int main() {
  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);
  int result = old_value + non_atomic_var;
  return result;
}
```
