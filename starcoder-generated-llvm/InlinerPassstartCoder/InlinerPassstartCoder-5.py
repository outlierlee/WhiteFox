
```cpp
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
/*
// Definition of a complex function that is not eligible for inlining
void complex_function(std::vector<int>& vec, int x) {
    std::transform(
      vec.begin(), vec.end(), vec.begin(), 
      [x](int y){ return y * x; } 
    );
}

int main() {
    std::vector<int> vec = {1, 2, 3}; // Initialize vector
    int x = 10; // Declare and initialize variable x
    int result = 0; // Declare and initialize variable result
    
    // Call the complex function and update result
    complex_function(vec, x); 
    std::for_each(vec.begin(), vec.end(), [&](int a){ result += a; });
    
    // Return the result of the function call
    return result; 
}
*/

// Definition of a function that the compiler might inline
static inline int small_function(int a, int b) {
    return a + b;
}

int main() {
    int x = 5; // Declare and initialize variable x
    int y = 10; // Declare and initialize variable y
    int result; // Declare variable to store the result

    // Call the small function and store the result
    result = small_function(x, y); 

    // Return the result of the function call
    return result;
}
```

