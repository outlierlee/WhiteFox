
```cpp
#include <vector>
#include <string>

int simple_conditional(int a, int b) {
  if (a > 0) {
    return b - 1;
  } else {
    return b + 1;
  }
}

int main() {
  int result = 0;
  int x = -42;
  int y = 18;
  int z = simple_conditional(-x, y);
  result = z;
  return result;
}
```

