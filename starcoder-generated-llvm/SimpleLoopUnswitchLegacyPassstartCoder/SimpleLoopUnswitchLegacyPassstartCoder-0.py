
```cpp
#include <vector>
#include <string>

// Define a function with a loop containing a condition
void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        if (flag) { // This condition should be invariant within the loop
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
    int flag = 1; // Invariant condition for the loop
    std::vector<int> vec = {0, 1, 2, 3};
    std::string str = "hello";
    vec.assign(5, 42);

    // Call the function with the loop
    loop_with_condition(n, flag);

    return 0;
}
```

In the generated C++ code, we explain that, in function `loop_with_condition`, there is a loop with an invariant condition. This simplified C++ code can be processed by a register-based processor where the loop can't be optimized away by the compiler if the `flag` does not change its value during the loop. The `main` function ensures that the `flag` is preserved as invariant across the function. The C code also involves some general loop unrolling and conditional jump.

