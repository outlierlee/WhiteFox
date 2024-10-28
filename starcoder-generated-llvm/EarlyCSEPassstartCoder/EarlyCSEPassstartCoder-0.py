
```cpp
#include <stdio.h>

const int SIZE = 10000;

int main() {
  int a = 10;
  int arr[SIZE] = {0};

  for (int i = 0; i < SIZE; i++) {
    arr[i] = a;
  }

  int result1 = 0;
  for (int i = 0; i < SIZE; i++) {
    result1 += arr[i];
  }
  
  // Redundant computation
  int result2 = 0;
  for (int i = 0; i < SIZE; i++) {
    result2 += arr[i];
  }

  printf("Result1: %d\n", result1);
  printf("Result2: %d\n", result2);
  
  return 0;
}
```

