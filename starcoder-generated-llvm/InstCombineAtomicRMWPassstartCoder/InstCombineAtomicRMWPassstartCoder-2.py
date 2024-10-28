
```cpp
#include <stdatomic.h>

int main() {
  atomic_int atomic_var = -1;

  atomic_fetch_add(&atomic_var, 213);

  return atomic_var;
}
```
