
```cpp
#include <stdatomic.h>

int main() {
  atomic_int atomic_var = 42;
  atomic_fetch_add(&atomic_var, 0);

  return 0;
}
```

