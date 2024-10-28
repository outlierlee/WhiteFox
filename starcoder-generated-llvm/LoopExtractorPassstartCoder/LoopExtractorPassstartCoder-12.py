
```c
#include <stdio.h>

void loop_function(int count) {
  int i;
  int sum = 0;
  
  for (i = 0; i < count; i++) {
    sum += i * 42; // something else
  }

  printf("Sum: %d\n", sum);
}

int main() {
  loop_function(256);

  return 0;
}
```

