
```cpp
#include<iostream>

static int my_function(int a, int b) {
  int result = 0;
  result = (a > b) ? a - b : b - a;
  return result;
}

int main() {
  int x = 20;
  int y = 30;
  int main_result = 0;

  main_result = my_function(x, y);

  return main_result;
}
```

