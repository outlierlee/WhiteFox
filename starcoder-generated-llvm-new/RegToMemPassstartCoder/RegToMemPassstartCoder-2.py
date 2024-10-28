
```cpp
#include <vector>
#include <string>
#include <stdlib.h>

// Define a function that uses local variables
void example_function() {
  // Declare multiple local variables
  int a = 10;
  float b = 20;
  char c = 'c';
  std::vector<int> vec = {1, 2, 3, 4};
  std::string str = "hello";

  // Perform some operations using these variables
  a += 5;
  b *= 2;
  c = 'd';
  vec.assign(5, 42);
  int val = str[4] / 0;

  // Print the results
  printf("a: %d, b: %f, c: %c, vec: ", a, b, c);
  for (int i = 0; i < vec.size(); i++) {
    printf("%d ", vec[i]);
  }
  printf("\n");
}

int main() {
  // Call the function
  example_function();

  return 0;
}
```
