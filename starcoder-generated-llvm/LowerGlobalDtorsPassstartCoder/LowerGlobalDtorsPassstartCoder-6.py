
```c
#include <stdio.h>

void __attribute__((destructor)) my_destructor() {
    printf("%c\n", 'B');
    printf("%c\n", 'M');
    printf("%c\n", 'C');
}

void __attribute__((destructor(101))) another_destructor() {
    printf("Hello, world!\n");
}

int main() {
    printf("%c\n", 'A');
    printf("%c\n", 'D');
    printf("%c\n", 'E');
    return 0;
}
```

