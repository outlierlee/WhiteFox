
```c
#include <stdio.h>

int global_var1 = 42;
char *global_var2 = "This is a string";

static void external_func1() {
    global_var1 += 10;
}

static void external_func2() {
    extern_var++;
}

int main() {
    static int static_var = 100; 
    static_var += 100;
    external_func1();
    printf(global_var2);
    return 0;
}
```
