
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* arg1, int* arg2) {
  int result = (*arg1) * 2 + (*arg2);
  return result;
}

int main() {
  int x = 50;
  int* ptr_x = &x;
  int y = 100;
  int* ptr_y = &y;
  int result = func_with_ptr_args(ptr_x, ptr_y);
  return result;
}
```

