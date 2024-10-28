
```c
#include <stdio.h>

inline float avg(float a, float b) {
  return (a + b) / 2.0;
}

int main() {
  float x = 5.5;
  float y = 10.5;
  float result = avg(x, y);
  printf("The average is: %.2f\n", result);
  return 0;
}
```

