
```cpp
#include <vector>
#include <string>

static int my_function(int a, int b) {
  int result = 0;
  if (a < b) {
    result = a;
  } else if (a > b) {
    result = b;
  } else {
    result = a;
  }
  return result * result;
}

int main() {
  int x = 42;
  int y = 69;
  int main_result = 0;
  main_result = my_function(x, y);
  return main_result;
}
```

