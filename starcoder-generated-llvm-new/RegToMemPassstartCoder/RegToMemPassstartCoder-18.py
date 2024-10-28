
```c
#include <stdio.h>

typedef struct {
  int x;
  float y;
} Point;

void example_function() {
  int a = 10;
  float b = 1.0;
  char c = 'c';

  Point p = {4, 5.2};
  p.x++;
  p.y--;

  printf("a: %d, b: %f, c: %c\n", a, b, c);

  if (p.x > 0 && p.y < 10.0) {
    printf("Point is inside the rectangle\n");
  }
}

int main() {
  example_function();
  return 0;
}
```

