
```cpp
#include <vector>
#include <string>

int main() {
  int x = -123;
  int y = 0;
  int z = 567;

  // Perform some operations that do not affect the final result
  int a = x + y; 
  int b = y * z; 

  // The final result is not related to a and b
  int result = x * z;

  return result;
}
```

