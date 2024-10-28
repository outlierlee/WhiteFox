
```cpp
#include <array>
#include <vector>
#include <algorithm>

// Define a function that contains a loop
void loop_function(std::array<int, 10>& arr) {
  for (auto& x : arr) {
    x = std::find(arr.begin(), arr.end(), x) - arr.begin();
  } // Obtain the distance to the first occurrence

  // Print the result to ensure the loop is not optimized away
  int sum = 0;
  for (const auto& x : arr) sum += x;
  printf("Sum: %d\n", sum);
}

int main() {
  std::array<int, 10> arr = {5, 7, 2, 9, 4, 1, 3, 8, 6, 0};

  // Call the function containing the loop
  loop_function(arr);

  return 0; // Return 0 to indicate successful execution
}
```

