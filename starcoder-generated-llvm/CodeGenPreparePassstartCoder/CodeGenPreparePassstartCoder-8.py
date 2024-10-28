
```c
#include <stdio.h>
#include <stdlib.h>

int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 1:
      result = x * x;
      break;
    case 2:
      result = x * x;
      break;
    default:
      result = x - 1;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int array[10];
  for (int i = 0; i < 10; i++)
    array[i] = i;

  int x = array[rand() % 10];
  main_result = switch_func(x);
  printf("%d\n", main_result);
  return main_result;
}
```

