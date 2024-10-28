
```cpp
#include <vector>
#include <string>
#include <cmath>

int main() {
  int x = 100000;
  int y = 300;

  while (x < 0) {
    y = y * x;
    x = abs(x - 15);
  }

  return x;
}
```

