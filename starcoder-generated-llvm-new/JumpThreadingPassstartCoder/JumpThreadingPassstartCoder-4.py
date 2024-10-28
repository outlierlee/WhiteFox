
```c
#include <stdio.h>

int simple_conditional(int a, int b) {
  if (a > 0) {
    return b + 1;
  } else {
    return b - 1;
  }
}

int main() {
  int x = 65000;
  int y = 42000;
  int result = 0;
  result = simple_conditional(x, y);
  if (result > 55000) {
    result = result / 2;
  } else {
    result = result * 2;
  }
  return result;
}
```

# End of C++ Code.