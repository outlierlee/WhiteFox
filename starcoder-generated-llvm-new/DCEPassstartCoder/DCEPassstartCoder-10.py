
```c
#include <stdio.h>

int x = 92384; // declare x
int y = 38400; // declare y
int z = 19023; // declare z

int main() {
  int main_result = 0; // declare the result

  int unused_var = x + y; // this operation is not used anywhere

  main_result = y / z; // perform some operation with y and z

  printf("%d\n", main_result); // print the result to ensure side effects

  return main_result; // return the result
}
```

