
```cpp
static int global_var = 217;

#include <cmath>

static int use_global_var() {
  global_var = std::abs(global_var);
  return global_var;
}

int main() {
  int result = 0;
  result = use_global_var();
  return result;
}
```

