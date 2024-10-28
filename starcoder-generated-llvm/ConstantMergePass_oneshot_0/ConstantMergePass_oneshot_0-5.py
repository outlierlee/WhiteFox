
```cpp
#include <vector>

static const int global_var1 = (1 << 31);
static const int global_var2 = ((1 << 15) - 1);

int main() {
  int result = 0;
  result = global_var1 + global_var2;
  std::vector<int> vec = {0, 1, 2, 3};
  vec.assign(5, global_var1);
  return result;
}
```

