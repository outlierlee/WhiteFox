
```cpp
#include <vector>
#include <string>

static int func_with_ptr_args(int* arg1, float* arg2, std::string* arg3) {
  int result = 10;
  if (*arg1 % 2) {
    result = *arg1 * 32 + 15;
  } else {
    result = *arg1 - 15;
  }
  if (*arg2 > 100) {
    result = result * 2;
  } else {
    result = result * 2;
  }
  if (arg3->size() > 1) {
    result = result + 10;
  } else {
    result = result - 10;
  }
  return result;
}

int main() {
  int result = 0;
  int a = (1 << 31);
  float b = 123456.78;
  std::string c = "hello";
  int* ptr_a = &a;
  float* ptr_b = &b;
  std::string* ptr_c = &c;
  result = func_with_ptr_args(ptr_a, ptr_b, ptr_c);
  return result;
}
```

