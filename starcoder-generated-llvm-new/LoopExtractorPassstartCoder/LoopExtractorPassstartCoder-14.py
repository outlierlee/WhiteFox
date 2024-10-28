
```c
#include <stdio.h>

static int opDispenser(int x, int y) { return x*y; }

static void loop_function() {
  int i;
  int sum = 0; 
  for (i = 0; i < 10; i++) {
    sum += opDispenser(i % 3, i % 2); 
  }
  printf("Sum: %d\n", sum);
}

int main() {
  loop_function();
  
  return 0;
}
```

