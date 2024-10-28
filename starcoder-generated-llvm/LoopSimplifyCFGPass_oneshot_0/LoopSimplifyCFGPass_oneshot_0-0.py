
```cpp
#include <vector>
#include <string>

int main() {
  int x = -123;
  int y = 0;
  int z = 5;

  while (x < y) {
    if (x == 3) {
      break;
    }
    x += 1;
    if (z == 4) {
      break;
    }
  }

  return x;
}
```

