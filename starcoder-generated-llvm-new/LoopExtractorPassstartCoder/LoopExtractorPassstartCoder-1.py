
```cpp
#include <iostream>
#include <vector>
#include <string>

// Define a function that contains a loop
static void loop_function(std::vector<int> arr, size_t initial_value = 0) {
  size_t sum = 0;
  for (auto &i : arr) {
    sum += i + initial_value;
  }
  std::cout << "Sum: " << sum << std::endl;
}

int main() {
  std::vector<int> arr(10, 0);
  for (int i = 0; i < 10; ++i) {
    arr[i] = i;
  }
  loop_function(arr, 5);

  return 0;
}
```

