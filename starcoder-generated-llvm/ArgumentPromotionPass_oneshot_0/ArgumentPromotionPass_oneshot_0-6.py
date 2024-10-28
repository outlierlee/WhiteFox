
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* arg1, std::string* arg2, float* arg3, std::vector<int>* arg4) {
  int result = *arg1;
  if (**arg2 == 12) {
    result = result * 3;
  } else {
    result = result + 5;
  }
  if (**arg2 >= 0) {
    result = result + 1;
  } else {
    result = result - 1;
  }
  if (**arg2 > 0) {
    result = result / *arg3;
  } else {
    result = result * 2;
  }
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 13);
  std::string str = "hello, world";
  std::vector<int> vect = {0, 1, 2, 3};
  int* ptr_a = &a;
  std::string* str_ptr = &str;
  std::vector<int>* vect_ptr = &vect;
  float f = 5.0f;
  float* ptr_f = &f;
  vect[3] = 12;
  result = func_with_ptr_args(ptr_a, str_ptr, ptr_f, vect_ptr); // you can pass the arguments with any number, any type
  return result;
}
```
