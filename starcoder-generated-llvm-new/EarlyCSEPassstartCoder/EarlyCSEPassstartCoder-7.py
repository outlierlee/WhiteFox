
```c
#include <stdio.h>
#define ITERATION_COUNT (5)

int main() {
  int arr[ITERATION_COUNT];
  for (int i = 0; i < ITERATION_COUNT; i++) {
    arr[i] = i * i;  // No benefit of optimizing this
  }
  int sum = 0;
  for (int j = 1; j <= ITERATION_COUNT; j++) {
    sum += arr[j];  // Will optimize to sum upto N terms
  }
  printf("Sum is: %d\n", sum);
  return 0;
}
```

