
```cpp
#include<stdio.h>

int main() {
    int changed = 0;
    int x = 100;
    int y = 500;

    // Unreachable code (always false)
    if(x == y) {
        changed = 1;
    }

    // Reachable code (never executed)
    while(x > y) {
        changed = 1;
    }

    // Print the value of `changed`
    printf("Changed is: %d\n", changed);
    return 0;
}
```

