
```c
#include <stdio.h>

int x = 2;

int main() {
  int main_result = 0;

  switch (x) {
    case 1:
      main_result = 10;
      break;
    case 2:
      main_result = 20;
      break;
    case 0:
      main_result = 0;
      break;
    default:
      main_result = 100;
      break;
  }

  return main_result;
}
```

