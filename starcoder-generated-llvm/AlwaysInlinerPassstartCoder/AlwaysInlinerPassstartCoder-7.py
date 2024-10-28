
```cpp
#include <string>
#include <iostream>
#include <algorithm>

inline std::string inline_func(std::string &str) {
  std::reverse(str.begin(), str.end());
  return str;
}

int main() {
  std::string result = "";
  std::string str = "hello";
  result = inline_func(str);
  return result[0];
}
```

