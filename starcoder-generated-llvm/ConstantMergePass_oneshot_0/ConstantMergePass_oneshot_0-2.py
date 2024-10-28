
```cpp
#include <vector>
#include <string>

static const int global_var1 = 1 << 31;
static const int global_var2 = ~global_var1 + 2;

int main() {
  using namespace std;
  int result = 0;
  int x = global_var1;
  int y = global_var2;
  if (x > y) {
    result = x - y;
  } else {
    result = y - x;
  }
  return result;
}
```
