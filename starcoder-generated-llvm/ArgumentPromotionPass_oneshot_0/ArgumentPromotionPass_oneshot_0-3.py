
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* arg1, int* arg2) {
  int result = 0;
  if(*arg1 % 2) result = *arg1 * 32 + 15; 
  else result = *arg1 - 15; 
  if(*arg2 > 100) result = result * 2;
  else result = result * 2;
  return result;
}

int main() {
  int x = (1 << 31);
  int y=18; 
  int* ptr_x = &x;
  int* ptr_y = &y;
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.assign(5, 42);
  int b = func_with_ptr_args(ptr_x, ptr_y);
  int result = b;
  return result;
}
```

