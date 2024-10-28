
```cpp
#include <stdio.h>

int func() {
    static int x = 10;
    return --x;
}

void __attribute__((destructor(103))) another_destructor() {
    static int x = 7;
    printf("Calling another_destructor [%d]\n", x);
    x = func();
    if (x < 0)
        puts("Error in execution");
}

void __attribute__((destructor(51))) third_destructor() {
    puts("Calling third_destructor");
}

int main() {
    static int x = 15;
    printf("Variable x = %d\n", x);
    return 0;
}
```

