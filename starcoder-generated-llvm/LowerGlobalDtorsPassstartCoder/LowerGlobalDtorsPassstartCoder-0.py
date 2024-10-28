
```c
#include <stdio.h>

void __attribute__((destructor)) dest1() {
    printf("Destructor 1\n");
}

void __attribute__((destructor(101))) dest2() {
    printf("Destructor 2\n");
}

int main() {
    printf("Main function\n");
    return 0;
}
```

