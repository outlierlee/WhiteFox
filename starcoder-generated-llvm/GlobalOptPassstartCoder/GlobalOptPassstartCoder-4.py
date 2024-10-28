
```c
#include <stdlib.h>
#include <time.h>

static int my_function(int a, int b) {
  srand(time(NULL));
  int result = 0;
  if (a > b) {
    result = a - b;
  } else {
    result = rand();
  }
  return result;
}

int main() {
  int x = 100, y = 15;
  int main_result = 0;

  if ((x & 1) == 0) {
    main_result = my_function(x, y);
  }

  return main_result;
}
```

