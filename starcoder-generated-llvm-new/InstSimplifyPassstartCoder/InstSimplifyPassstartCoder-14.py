
```c
#include <stdio.h>

static int a = 2560;
static int b = 160;

int main() {
  int result = 0;

  if (b != 0){
    result = a / b;
  }else{
    result = 0;
  }

  int redundant = a % 2;

  printf("Result: %d, Redundant: %d\n", result, redundant);

  return 0;
}
```

