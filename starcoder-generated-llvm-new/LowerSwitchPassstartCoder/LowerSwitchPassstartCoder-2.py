
```cpp
#include <stdio.h>

// declare variables
int x = -5;

int main() {
  int main_result = 0;

  switch (x) {
    case 3:
      main_result = 30;
      break;
    case 5:
      main_result = 50;
      break;
    case -1:
      main_result = -10;
      break;
    default:
      main_result = 0;
      break;
  }

  return main_result;
}
```
