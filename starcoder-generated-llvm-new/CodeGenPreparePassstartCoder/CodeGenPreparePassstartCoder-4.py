
```cpp
#include <stdio.h>

int switch_func(int x) {
  int result = 0;
  switch (x) {
    case 5:
      result = x + 5;
      break;
    case 10:
      result = x + 10;
      break;
    default:
      result = x + 20;
      break;
  }
  return result;
}

int main() {
  int main_result = 0;
  int arr[] = {2,4,6,8,10,12};
  int x = arr[1] * arr[2];
  main_result = switch_func(5);
  printf("%d\n", main_result);
  return main_result;
}
```

