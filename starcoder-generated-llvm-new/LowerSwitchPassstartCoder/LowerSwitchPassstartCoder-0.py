
```cpp
#include <stdio.h>

int x = 15;

int main() {
  int main_result = 0;

  switch (x) {
    case 5:
      main_result = 1;
      break;
    case 10:
      main_result = 2;
      break;
    case 15:
      main_result = 3;
      break;
    default:
      main_result = 4;
      break;
  }

  return main_result;
}
```
