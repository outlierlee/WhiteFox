
```cpp
#include <array>
#include <vector>
#include <string>

// Define a function with a simple conditional structure
int simple_conditional(int a, int b, int idx) {
  int result = b;
  if(idx > 1) {
    result += 2;
  } else {
    result -= 2;
  }
  // Obtain the result based on the value of a and return it
  if (a > 0) {
    result += 1;
  } else {
    result -= 1;
  }
  return result;
}

int main() {
  int x = 5; // Initialize variable x
  int y = 2; // Initialize variable y
  int idx = 1; // Initialize variable idx
  int result; // Declare result variable

  // Call the function with a constant condition
  result = simple_conditional(x, y, idx);

  // Use the result in a conditional branch
  if ((x > 0 && idx <= 2 && y==2) && (result > 5)) {
    printf("Result is greater than 5\n");
  } else {
    printf("Result is less than or equal to 5\n");
  }

  return result;
}
```
