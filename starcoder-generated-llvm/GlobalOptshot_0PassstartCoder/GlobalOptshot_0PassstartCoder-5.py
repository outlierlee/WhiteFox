
```c
#include <stdlib.h>

static int my_function(int a, int b) {
  int difference = abs(a - b);
  int sum = a + b;
  if (difference == 1) {
    return difference * sum;
  } else {
    return difference / sum;
  }
}

int main() {
  int result = 0;
  result = my_function(156, 167);
  return result;
}
```

