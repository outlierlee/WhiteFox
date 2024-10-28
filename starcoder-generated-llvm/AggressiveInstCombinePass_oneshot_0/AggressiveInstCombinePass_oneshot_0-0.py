
```cpp
#include <vector>
#include <string>

int func(int x, int y) {
  int result = x + y;
  if (x < y) {
    result += x;
  } else {
    result -= y;
  }
  result *= (x >> 1);
  if (result > 42){
    result -= 26;
  }
  else {
    result += 26;
  }
  return result;
}

int main() {
  int result;
  int x = (1 << 30);
  int y = 6;
  std::vector<int> vec = {0, 1, 2, 3};
  std::string str = "hello";
  vec.insert(vec.end(),5, y);
  int z = func(x,y);
  result = static_cast<short>(z);
  return result;
}
``` 

