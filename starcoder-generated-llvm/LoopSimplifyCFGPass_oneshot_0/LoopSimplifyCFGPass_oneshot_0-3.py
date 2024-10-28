
```cpp
#include <vector>
#include <string>

int main() {
  int x = (1 << 18);
  int y = 40;
  int z = (1 << 6);
  while (x < y) {
    int i = x>0 ? 1 : 0;
    x += i;
    if (z == (1 << 31)) {
      break;
    }
  }
  return 0;
}
```

