
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* arg1, int* arg2, int* arg3) {
  int result = 0;
  if (*arg1 > *arg2 * *arg3) {
    result = *arg1 - *arg2 - *arg3;
  } else {
    result = *arg1 + *arg2 - *arg3;
  }
  if (*arg1 > 100) {
    result = result * 2;
  } else {
    result = result - 2;
  }
  return result;
}

int main() {
  int result = 0;
  int x = (1 << 31);
  int y = -1;
  int z = 3;
  int* ptr_x = &x;
  int* ptr_y = &y;
  int* ptr_z = &z;
  result = func_with_ptr_args(ptr_x, ptr_y, ptr_z);
  return result;
}
```

