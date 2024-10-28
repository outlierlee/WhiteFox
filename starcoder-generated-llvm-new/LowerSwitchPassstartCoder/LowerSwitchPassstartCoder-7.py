
```c
#include <stdio.h>

int x = (1 << 31);

int main() {
  int main_result = 0;

  switch (x) {
    case 1:
      main_result = 25;
      break;
    case 2:
      main_result = 50;
      break;
    case 3:
      main_result = 100;
      break;
    default:
      main_result = 150;
      break;
  }
  return main_result;
}
```

