
```cpp
#include <vector>
#include <string>

int main() {
  int x = (1 << 18);
  int y = (1 << 18);
  int z = (1 << 10);

  int *p = new int;
  *p = x + y + z;

  int result = *p;
  delete p;
  
  return result;
}
```

