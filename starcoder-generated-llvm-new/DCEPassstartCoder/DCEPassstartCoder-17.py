
```c
#include <stdio.h>

int main() {
  int main_result = 0;
  int x = 10; // declare variable x
  int y = 20; // declare variable y
  int z = 30; // declare variable z

  // perform some operations that result in dead code
  int unused_var = 4 - x;

  // use some variables in a way that does not affect the unused_var
  main_result = y + z;

  printf("%d\n", main_result);

  return main_result;
}
```

