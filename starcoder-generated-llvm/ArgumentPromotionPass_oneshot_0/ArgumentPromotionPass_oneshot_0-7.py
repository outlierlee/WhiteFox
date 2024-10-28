
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* arg1, int* arg2, int* arg3, int* arg4) {
  int result = 0;
  if (*arg1 > *arg2) {
    if (*arg1 % 2) {
      *arg2 = *arg4 * 3 - 15;
    } else {
      *arg2 = *arg4 * 5 + 5;
    }
  } else {
    *arg1 = *arg2 + 15;
  }
  result = *arg1 + *arg2 + *arg3;
  return result;
}

int main() {
  int result = 0;
  int x = (1 << 30);
  int y = (1 << 31);
  int z = 42;
  int* ptr_x = &x;
  int* ptr_y = &y;
  int* ptr_z = &z;

  std::vector<int> vec(3);
  for (int i = 0; i < 3; i++) {
    vec[i] = (1 << i);
  }
  int* ptr_vec = &vec[0];
  result = func_with_ptr_args(ptr_x, ptr_y, ptr_vec, ptr_z);
  return result;
}
```
