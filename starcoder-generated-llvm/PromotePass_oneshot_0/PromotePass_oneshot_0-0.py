
```cpp
#include <vector>
#include <string>

int main() {
  int x = -123;
  int y = 456;
  int z = 789;

  int *p = new int;
  *p = x + y + z;

  int result = *p;
  delete p;

  return result;
}
```

