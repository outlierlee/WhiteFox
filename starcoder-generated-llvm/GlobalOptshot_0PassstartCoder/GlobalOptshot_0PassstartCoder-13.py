
```c++
#include <string>
#include <vector>

// Define a function without a specific calling convention
static __attribute__((fastcall)) int my_function(int a, int b, int c, double d, char e) {
  if (a > b) {
    return static_cast<int>(d) - c + e;
  } else {
    return a & b & c & d & e;
  }
}

int main() {
  int result = 0;
  int x = 2;
  int y = 3;
  int z = 4;
  double w = 10.0;
  std::string str = "hello";
  std::vector<int> vec = {1, 2, 3, 4};
  result = my_function(x, y, z, w, str[x + 5]);
  vec[y / z] = my_function(z, x, y, z + w, str[y]);
  result = vec[z / x];
  return result;
}
```

