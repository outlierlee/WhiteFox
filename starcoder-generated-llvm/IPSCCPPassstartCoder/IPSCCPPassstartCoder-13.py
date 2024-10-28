
```c
#include <stdio.h>

static int global_var = 42;

static int use_global_var() {
  char my_char = 'a';
  int my_int = global_var * 2;
  printf("the double value of global_var is %d\n", my_int);
  return my_int;
}

int main() {
  int result = 0;
  result = use_global_var();
  result++;
  return result;
}
```

