```c
#include <stdio.h>

int x = sizeof(int) + sizeof(float) - sizeof(char);

int main() {
  int main_result = 0;

  signed int unsigned_var = 5;
  unsigned int signed_var = -7;

  main_result = unsigned_var + signed_var;

  printf("%d\n", main_result);

  return main_result;
}
```

