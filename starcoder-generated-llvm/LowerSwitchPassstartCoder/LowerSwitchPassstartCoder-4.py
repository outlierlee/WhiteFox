
```cpp
#include <stdio.h>

int x = -20; // declare x
int main() {
  int main_result;

  switch (x) {
    case -20:
      printf("The case is -20\n");
      main_result = 0;
      break;
    case 5:
      printf("The case is 5\n");
      main_result = 1;
      break;
    case -542:
      printf("The case is -542\n");
      main_result = 2;
      break;
    default:
      printf("The case is other\n");
      main_result = x;
      break;
  }
  return main_result;
}
```
