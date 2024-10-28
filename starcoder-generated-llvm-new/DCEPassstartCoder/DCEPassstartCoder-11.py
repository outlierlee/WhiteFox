
```c
#include <stdio.h>

#define OPERATOR +
#define ANY_VALUE 43
#define ANY_TYPE int

int x = ANY_VALUE;
ANY_TYPE y = ANY_VALUE;
ANY_TYPE z = ANY_VALUE;

int main() {
  int main_result = 0;

  int unused_var = x OPERATOR ANY_VALUE;

  main_result = y OPERATOR z;

  printf("%d\n", main_result);

  return main_result;
}
```

