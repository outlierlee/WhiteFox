
```c
#include <stdio.h>

int main() {

  int x = 10; // case 1

  switch (x) {
    case 5:
      printf("%d\n", 50);
      return 50;
    case 10:
      printf("%d\n", 100);
      return 100;
    case 15:
      printf("%d\n", 150);
      return 150;
    default:
      printf("%d\n", 200);
      return 200;
  }
}
```
