
```c
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 100:
      result = x * x;
    case 200:
      result = result * result;
    case 300:
      result = result / result + 1;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int x = 231;
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```

