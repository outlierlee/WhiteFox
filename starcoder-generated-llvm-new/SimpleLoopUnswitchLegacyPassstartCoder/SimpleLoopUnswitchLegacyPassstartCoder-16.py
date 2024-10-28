
```cpp
#include <array>
#include <vector>
#include <string>

// Define a function with a loop containing a condition
void loop_with_condition(int n, int invariant_flag) {
    for (int i = 0; i < n; ++i) {
        if (invariant_flag) { // This condition should be invariant within the loop
            // Perform some operations
            printf("Flag is true, iteration %d\n", i);
        } else {
            // Perform some other operations
            printf("Flag is false, iteration %d\n", i);
        }
    }
}

int main() {
    int n = 10; // Loop iteration count
    int invariant_flag = 1; // Invariant condition for the loop

    // Call the function with the loop
    loop_with_condition(n, invariant_flag);

    return 0;
}
```
