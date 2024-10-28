
```cpp
#include <stdatomic.h>
#include <string>

int main() {
  atomic_int atomic_var = 5;
  int non_atomic_var = 10;
  std::string str = "hello";

  int old_value = atomic_fetch_add(&atomic_var, non_atomic_var);

  int result = old_value ? (old_value * 2) : (old_value / 2);

  return result;
}
```
