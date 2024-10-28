
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* arg1, int* arg2, int* arg3) {
  int result = 10;
  if (arg1[0]) {
    result = arg1[1] * 32 + arg2[2];
  } else {
    result = arg1[2] - arg3[3];
  }
  if (arg1[0] > 100) {
    result = result * 2;
  } else {
    result = result * 2;
  }
  return result;
}

int main() {
  int result = 0;
  int x = (1 << 31);
  int y = (1 << 31) + 1;
  int z = (1 << 31) + 2;
  int* x_ref = &x;
  int* y_ref = &y;
  int* z_ref = &z;
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  int result_ = func_with_ptr_args(x_ref, y_ref, z_ref);
  result = result_;
  return result;
}
```
