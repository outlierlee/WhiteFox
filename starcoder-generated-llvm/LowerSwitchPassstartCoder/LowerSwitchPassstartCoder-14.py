
```c
#include <stdio.h>

int x = 5;

int main() {
  int main_result = 0;

  switch (x) {
    case 1:
      main_result = 11;
      break;
    case 2:
      main_result = 22;
      break;
    case 3:
      main_result = 33;
      break;
    case 4:
      main_result = 44;
      break;
    case 5:
      main_result = 55;
      break;
    default:
      main_result = 0;
      break;
  }

  return main_result;
}
```

