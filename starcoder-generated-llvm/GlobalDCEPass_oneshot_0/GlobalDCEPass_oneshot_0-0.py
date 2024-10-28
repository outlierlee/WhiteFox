
```cpp
#include <vector>
#include <string>

void unused_func() {
  printf("arithmetic: %.3f\n", 5.0 * 6.0 / 7.0);
  printf("%s\n", "unused_func() method called");
}

int main() {
  int x = 0;
  while (x < 10) {
    x += 1;
  }
  
  std::vector<int> vec = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  std::string str = "main_func() method called";
  for (int i = 0; i < vec.size(); ++i) {
    if (i % 2 == 0) {
      unused_func();
    }
    printf("index: %d, val: %d\n", i, vec[i]);
  }
  printf("%s\n", str.c_str());
  
  return (x + vec[0] + vec[vec.size() / 2] + *str.c_str()) % 2;
}
```
