
```cpp
#include <string>

static const int global_var1 = 1024;
static const std::string global_var2 = "hello";

int main() {
  int result = 0;
  int x = global_var1;
  std::string y = global_var2;
  result = x + y.size();
  return result;
}
```
