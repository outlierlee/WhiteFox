
```cpp
#include <iostream>
using std::cout;

void fill_arr(int* arr, int size, int pattern) {
  for (int i = 0; i < size; ++i) {
    arr[i] = pattern + i;
  }
}

int main() {
  int x = 5;
  int y = 0;
  int z = 1;

  int arr[x];
  fill_arr(arr, sizeof(arr) / sizeof(arr[0]), z);

  for (int i = 0; i < x; ++i) {
    y += arr[i];
    z += i;
  }

  return y;
}
```

