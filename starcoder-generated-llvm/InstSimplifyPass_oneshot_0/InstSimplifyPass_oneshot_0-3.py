
```cpp
#include <vector>
#include <string>

int main() {
  int x = (1 << 18);
  int y = (1 << 18);
  int z = x + y;
  if (z == x + y) {
    z += x;
  }
  return z;
}
```

