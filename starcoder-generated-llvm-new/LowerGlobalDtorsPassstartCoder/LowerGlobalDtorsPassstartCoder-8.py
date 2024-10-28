
```c
#include <stdio.h>

__attribute__((destructor(100))) static void destructor_100() {
    printf("Destructor 100\n");
}

__attribute__((destructor)) static void regular_destructor() {
    printf("Regular destructor\n");
}

__attribute__((destructor(123))) static void destructor_123() {
    printf("Destructor 123\n");
}

__attribute__((destructor(1))) static void lowest_priority() {
    printf("Lowest priority and later\n");
}

__attribute__((destructor(1000))) static void highest_priority() {
    printf("Highest priority and later\n");
}

int main() {
    printf("In main function, do some computation...\n");
    return 0;
}
```

