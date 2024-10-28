
```c
#include <stdio.h>

void __attribute__((destructor)) my_destructor() {
    int a = (3 << 25);
    float b = 1.5666f;
    printf("Destructor 1 is called with argument: %d and %f\n", a, b);
}

void __attribute__((destructor(102))) another_destructor() {
   int c = (1 << 8);
   printf("Destructor 2 is called with argument: %d\n", c);
}

int main() {
    printf("Main function is printed first\n");
    return 0;
}
```

