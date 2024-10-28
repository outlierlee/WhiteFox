
```cpp
#include <vector>
#include <string>
#include <list>
#include "unordered_set"

typedef struct {
  int x;
  int y;
} Pair;

int func_with_unused_params(int a, int b, int c) {
  int result = 0;
  result = a + b + c;
  return result;
}

int main() {
  int x = 2;
  int y = 3;
  int z = 4;
  int main_result = 0;

  int a[] = {1, 2, 3, 4, 5};
  std::vector<int> vec = {1, 2, 3, 4};
  std::list<std::string> li = {"hello", "world"};
  std::unordered_set<Pair*> set;

  main_result = func_with_unused_params(a[0], vec[1], li.size());
  return main_result;
}
```

