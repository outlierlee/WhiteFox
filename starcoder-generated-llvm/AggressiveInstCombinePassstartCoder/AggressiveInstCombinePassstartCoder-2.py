
```cpp
#include <stdio.h>
#include <math.h>

static int trunc_func(int a, int b, float c) {
  int result = 0;
  result = (int)(sqrt((double)a)) + b;
  result = (sqrt(a) + b) * c;
  return result;
}

int main() {
  int a = (1 << 31); // define the variables
  int b = -(1 << 31);
  float c = 10.5;
  int main_result = 0; // declare the result
  main_result = trunc_func(a, b, c); // invoke the function
  printf("%d\n", main_result); // print the result
  return 0;
}
```

