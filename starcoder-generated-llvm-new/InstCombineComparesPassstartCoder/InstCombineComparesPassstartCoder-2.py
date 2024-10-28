```
#include <stdio.h>

#define MaxArraySizeForCombine 10000
#define ARRAY_SIZE 150

const int global_array[ARRAY_SIZE] = {1, 2, 3, 4};

int main() {
  int result = 0;
  for (int i = 0; i < ARRAY_SIZE; ++i) {
    if (global_array[i] != 0) {
      result = i*3;
    }
  }
  return result;
}
```
