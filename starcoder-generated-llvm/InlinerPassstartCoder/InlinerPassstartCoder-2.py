
```cpp
#include <vector>
#include <string>
#include <stdlib.h>

// Define a function that is small and simple enough to be inlined
static inline int simple_function(int a, int b) {
    return a + b; // Simple operation that can be easily inlined
}

int main() {
    int result = 0; // Declare and initialize variable result to store the result
    int x = abs(1 << 31); // Declare and initialize variable x
    std::vector<int> vec = {0, 1, 2, 3}; // Declare and initialize a vector
    std::string str = "hello"; // Declare and initialize a string
    vec.assign(5, 42); // Assign 42 to five elements of vec

    // Call the simple_function with x and vec[1] as arguments
    result = simple_function(x, vec[1]);

    // Return the result of the function call
    return result;
}
```

