
```c
#include <stdio.h>

int main() {

  int x = -1;
  int y = 30;
  int z = 15;
  int unused_var = x - y; // this operation is not used anywhere
  int main_result = y * z; // y and z are used in main_result

  printf("%d\n", main_result); // ensure side effects

  return main_result; // return the result
}
```

