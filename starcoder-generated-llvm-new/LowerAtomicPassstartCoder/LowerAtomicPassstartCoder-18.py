
```cpp
#include<stdatomic.h>

atomic_int atomic_var = (1 << 31);

int main() {
  int old_value = atomic_fetch_add(&atomic_var, (1 << 31));
  int result = old_value * 2;

  return result;
}
```
