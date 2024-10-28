
```cpp
#include <vector>
#include <string>

static const int global_var1 = (1 << 31);
static const int global_var2 = - (1 << 31);

int main() {
  int result = 0;
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  int x = global_var1;
  int y = global_var2;
  result = x + y;
  return result;
}
```
