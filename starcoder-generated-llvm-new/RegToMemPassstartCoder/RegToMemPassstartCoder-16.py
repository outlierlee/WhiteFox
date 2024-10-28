
```cpp
#include <stdio.h>

// Define two arrays and a function
const int SIZE = 10;
int arr1[SIZE] = {0};
float arr2[SIZE] = {0};
void function_with_array_args() {
  float sum = 0, avg;
  // perform some operations using the arrays
  for (int i = 0; i < SIZE; i++) {
    arr1[i] = i*2;
    arr2[i] = arr1[i] * 1.23;
    sum += arr2[i];
  }
  printf("sum of array2: %f\n", sum);
}

// Define a structure and perform operations on its members
struct MyStruct {
  int memberOne;
  float memberTwo;
  char memberThree;
};
void function_with_struct_args(MyStruct s) {
  // perform some operations using the struct members
  s.memberOne += 3;
  s.memberTwo *= 2.0;
  s.memberThree = 'b';
  printf("memberOne: %d, memberTwo: %f, memberThree: %c\n", s.memberOne, s.memberTwo, s.memberThree);
}

int main() {
  function_with_array_args();

  MyStruct myStr;
  myStr.memberOne = 5;
  myStr.memberTwo = 6.0;
  myStr.memberThree = 'a';
  function_with_struct_args(myStr);

  return 0;
}
```
