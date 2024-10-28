
```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

static int unused_function() {
  int result = 0; 
  int variable = -10;
  if (variable < 20) {
    result = variable * 2;
  } else {
    result = variable - 2;
  }
  if (variable > 5) {
    result = result / 2;
  } else {
    result = result * 2;
  }
  return result;
}

int main() {
  srand(time(NULL));
  int main_result = 0;
  std::vector<int> vec = {0, 1, 2, 3};
  int a = vec[rand() % vec.size()];
  RANDOM_CODE:
  main_result = a + 5;
  return main_result;
}
```

