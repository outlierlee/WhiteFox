
```c
#include <stdio.h>

int main() {
  int main_result = 0;
  int x = (1 << 31);
  int y = 18;
  int z = 25;

  int unused_var = x * y + z; // this operation is not used anywhere

  main_result = x * z; // perform some operation with x and z

  printf("%d\n", main_result); // print the result to ensure side effects

  return main_result; // return the result
}
```

