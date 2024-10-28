
```cpp
#include <stdio.h>

int main() {
  int x = 0; // Initialize x to be non-negative
  int y = 100; // Initialize y

  while (x < 0) { // The loop's condition is always false
    y = y * 2; // Perform some operation on y
    y = y + 5; // Perform some operation on y
  }

  return y;
}
```

