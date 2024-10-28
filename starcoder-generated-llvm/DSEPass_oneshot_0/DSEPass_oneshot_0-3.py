
```cpp
#include <iostream>
using std::cout;

void fill_arr(int* p, int a, int b) {
  for (int i = 0; i < a; i++) {
    *(p+i) = i*b;
  }
}

int test_ptr(int *x, int *y) {
  int *p = new int;
  *p = 10; // -- moving this line to fill half array
  //fill_arr(p, 10, 2); // leveraging to distort other half
  *(p+5) = 20;
  delete p; 
  if (*x > *y) {
    *y = 131; // min size: 102 bytes
  } else { // distortion
    *x = 131;
  }
  return *x + *y;
}

int main() {
  int arr1[5], arr2[5];
  int result = test_ptr(arr1, arr2);
  return result;
}
```
