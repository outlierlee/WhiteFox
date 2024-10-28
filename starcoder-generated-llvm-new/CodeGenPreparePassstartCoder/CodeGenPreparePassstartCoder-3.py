
```c
#include <stdio.h>


// Define a function with a switch statement
int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 3:
      result = x + 11;
      break;
    case 100:
      result = x + 20;
      break;
    default:
      result = x + 33;
      break;
  }
  return result;
}

int main() {
  int x = 111;
  int main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```

