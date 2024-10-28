
```c
#include <stdio.h>

void __attribute__((destructor(105))) third_destructor() {
    printf("Third destructor called\n");
}

void __attribute__((destructor(102))) second_destructor() {
    printf("Second destructor called\n");
}

void __attribute__((destructor(101))) first_destructor() {
    printf("First destructor called\n");
}

int main() {
    printf("Main function\n");
    return 0;
}
```

