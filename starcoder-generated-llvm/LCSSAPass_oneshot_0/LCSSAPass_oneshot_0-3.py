
```cpp
#include <vector>
#include <string>

int main() {
  int x = (1 << 18);
  int y = 40;
  int z = -10;
  int result = 0;
  int i = 5;

  for (i = 0; i < 50; i++) {
    if (i % 2) {
      result += x + y;
    } else {
      result += z;
    }
  }

  // this will cause latest value of result to be pick in return statement to utilized SSAL 
  std::vector<int> vec(10, result);
  std::string str = "Hello world";

  return result;
}
```

