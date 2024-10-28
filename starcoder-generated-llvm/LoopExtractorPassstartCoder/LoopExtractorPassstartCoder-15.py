
```c
#include <stdio.h>

#define NUM_ELEMS (50000)

void loop_function() {
  int i;
  long long sum = 0;
  for (i = 0; i < NUM_ELEMS; i++) {
    sum += i;
  }
  printf("Sum: %lld\n", sum);
}

int main() {
  loop_function();
  return 0;
}
```

