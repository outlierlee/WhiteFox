
```c
#include <alloca.h>
#include <stdio.h>

static void varargs_func() {
  int x = 100;
  int* ptr = (int*)alloca(sizeof(int)); // allocate stack memory
  *ptr = x; // use the allocated memory

  for (int i = 0; i < x; ++i) { // loop depends on 'x'
    *ptr += i; // use the allocated memory
  }

  printf("result: %d\n", *ptr); // print used memory
}

int main() {
  varargs_func();
  return 0;
}
```
