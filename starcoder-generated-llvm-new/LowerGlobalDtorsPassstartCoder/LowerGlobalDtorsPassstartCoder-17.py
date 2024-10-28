
```c
#include <stdio.h>

void __attribute__((destructor)) my_destructor() {
    printf("my_destructor called\n");
}

void __attribute__((destructor(101))) another_destructor() {
    printf("another_destructor called\n");
}

void __attribute__((constructor)) static_intialization_fnc() {
    printf("static initialization function\n");
}

int main() {
    printf("main function\n");
    return 0;
}
```
