
```c
#include <stdio.h>

int x = 10; // declare x
int y = 20; // declare y
int z = 30; // declare z

int main() {
  int main_result = 0; // declare the result

  // perform some operations that result in dead code
  int unused_var = x - y; // this operation is not used anywhere

  // use some variables in a way that does not affect the unused_var
  main_result = y + z; // perform some operation with y and z

  printf("%d\n", main_result); // print the result to ensure side effects

  return main_result; // return the result
}
```
