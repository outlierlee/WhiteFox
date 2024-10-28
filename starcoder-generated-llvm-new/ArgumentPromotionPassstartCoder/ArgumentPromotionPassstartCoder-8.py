
```c
#include <stdio.h>
#include <stdlib.h>

static int sum_array(int *arr, int n) {
  int sum = 0;
  for (int i = 0; i < n; i++) {
    sum += arr[i];
    if (arr[i] % 2 == 0) {
      arr[i] *= 2;
    }
  }
  return sum;
}

int main() {
  int arr[] = {1, 2, 3, 4, 5, 6};
  int len = sizeof(arr) / sizeof(arr[0]);
  
  int sum = sum_array(arr, len);
  
  int sum_after = 0;
  for (int i = 0; i < len; i++) {
    sum_after += arr[i];
  }
  
  int diff = sum_after - sum;
  
  printf("Array Sum before: %d, Array Sum after: %d, Difference: %d\n", sum, sum_after, diff);
  
  return 0;
}
```

