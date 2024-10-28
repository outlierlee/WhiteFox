
```c
#include <stdio.h>

float a = 92.10; // declare a
float b = 3.000; // declare b
int c = 100; // declare c

static float trunc_func(float a, float b, int c) {
  float result = 0; 
  if (c % 2 == 0) {
    result = ((int)a % (int)b) * c; // truncating mechanism is present
  } else {
    result = ((int)b % (int)a) * c; // truncating mechanism is present
  }
  return result;
}

int main() {
  float main_result = 0; 
  main_result = trunc_func(a, b, c);
  printf("%f\n", main_result); // print the result
  return 0;
}
```

