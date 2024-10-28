
```cpp
#include <iostream>
#include <vector>
#include <array>
#include <string>
/*
// declare variables
int x = -1; 
int y = -1; 
std::vector<std::array<int, 3>> vec = {{1, 2, 3}, {4, 5, 6}};
std::string str = "hello";
*/

int garbage_call_with_unused_variable(int x) {
  return x + 1;
}

int main() {
  int main_result = 0;
  int unused_var = x / y;
  main_result = garbage_call_with_unused_variable(unused_var) * vec[0][1] * str.length();
  printf("%d\n", main_result);
  return main_result;
}
```

