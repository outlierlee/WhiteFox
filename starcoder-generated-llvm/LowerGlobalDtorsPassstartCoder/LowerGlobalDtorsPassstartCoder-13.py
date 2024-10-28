
```c
#include <stdio.h>

int var_int __attribute__((destructor(100)));
extern void (*dtor100)(void);

void __attribute__((destructor(101))) another_destructor() {
    printf("Another destructor was called\n");
}

int main(void) {
    printf("Main function\n");
    return 0;
}
```

