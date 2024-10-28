
```cpp
#include <string>
#include <vector>
#include <sstream>

int global_var1 = 128; // An integer with a large enough initial value of concern to cause optimization
std::vector<int> global_var2 = {1,2,3,4,5}; // An integer array with a large enough initial value of concern to cause optimization
std::string global_var3 = "Hello, world!"; // A string with a large enough initial value of concern to cause optimization

namespace {
void external_func1() {
  std::stringstream ss;
  ss << global_var1 << ", " << global_var3;
  global_var3 = ss.str();
}

void external_func2() {
  global_var1 = 0;
  global_var2[0] = -500;
  global_var2[1] = -456;
  global_var2[2] = -142;
  global_var2[3] = -89;
  global_var2[4] = -5;
}
}

int main() {
  global_var1 = global_var1 + 10; // Potentially cause optimum
  external_func1();
  external_func2();
  return 0;
}
```
