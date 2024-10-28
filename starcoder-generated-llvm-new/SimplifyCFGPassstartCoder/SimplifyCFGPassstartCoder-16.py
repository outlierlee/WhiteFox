
```cpp
#include <stdbool.h>
#include <stdio.h>

int main() {
    bool Changed = false; // Preset value status to be false 
    int x = 0; // variable.
    int y = 1; // variable.

    // A simple conditional structure that creates an unreachable block
    if (x > y) { // Condition is always false
        Changed = true; // The variable only gets here when it's false due to the condition being never true.
        printf("Unreachable block\n");
    } else { // This block is reachable
        printf("Reachable block\n");
    }

    // A loop that never executes, creating another unreachable block
    while (x > y) {
        Changed = true; // variable is set to true using an unreachable loop
        printf("Unreachable loop block\n");
    }

    return 0;
}
```

Here the code deletes all unreachable blocks thereby causing the boolean variable `Changed` to become `true`, creating an opportunity for optimization.

