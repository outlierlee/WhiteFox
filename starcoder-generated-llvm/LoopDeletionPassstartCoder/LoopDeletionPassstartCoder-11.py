
```c
#include <stdio.h>

int main() {
  int x = -10; // Example value where loop condition always false
  int y = 0;

  while (x < 0) { // The condition is always false
    y = y + 42; // Example operation that does not change loop's execution
  }

  return (y * 2); // Return value is related to loop
}
```

