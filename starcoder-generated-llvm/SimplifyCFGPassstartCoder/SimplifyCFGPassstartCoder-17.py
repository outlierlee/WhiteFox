
```c
#include <stdio.h>

// A function that is never called
static void never_called() {
    int a = 1, b = 2;
    a += b;
}

int main() {
    // declaring a variable
    int x = 0;
    
    // entering a loop that will never be executed
    while (1) {
        x++;
    }

    return 0;
}
```

# C Code ends

