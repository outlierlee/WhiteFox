
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* x, float* y, const char* str, std::vector<int>* vec) {
  int result = 10;
  if (*x % 2) {
    result = *x * *y + 15;
  } else {
    result = *x - 15;
  }
  if (*x > 100) {
    result = result * 2;
  } else {
    result = result * 2;
  }
  if (str[0] == 'h') {
    result = result * 3;
  } else {
    result = result * 4;
  }
  if(vec[1] == 42) {
    result -= 10;
  } else {
    result += 10;
  }
  return result;
}

int main() {
  int result = 0;
  int x = (1 << 31);
  int y = 111;
  std::string str = "hello";
  std::vector<int> vec = {0, 1, 2, 3};
  vec.assign(5, 42);
  result = func_with_ptr_args(&x, &y, &str[0], &vec);
  return result;
}
```
