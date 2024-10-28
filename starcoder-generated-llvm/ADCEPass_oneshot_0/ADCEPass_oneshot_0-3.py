
```cpp
#include <vector>
#include <string>

int main() {
  int x = (1 << 18);
  int y = (1 << 18);
  int z = (1 << 10);

  int a = x + y;
  int b = y * z;

  int result = x * z;

  return result;
}
```

