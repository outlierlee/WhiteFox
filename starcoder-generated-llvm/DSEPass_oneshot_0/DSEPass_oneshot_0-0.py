
```cpp
#include <vector>
#include <string>

int main() {
  int *p = new int;
  *p = 10;
  *p = 20;
  delete p;
  return *p; // IT WILL BYE BUG as the memory location p is freed
}
```

# C++ code ends