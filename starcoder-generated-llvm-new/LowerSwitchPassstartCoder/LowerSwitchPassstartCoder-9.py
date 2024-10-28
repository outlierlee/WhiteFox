
```c
#include <stdio.h>

int x = 3;

int main() {
  int main_result = 0;

  switch (x) {
    case 1:
      main_result = 10;
      break;
    case 2:
      main_result = 20;
      break;
    case 3:
      main_result = 5;
      break;
    default:
      main_result = 400;
      break;
  }

  return main_result;
}
```
