
```c
#include <stdio.h>

static int g_var = 1;

void __attribute__((destructor(101))) my_destructor() {
    g_var = g_var * 10 + 5;
    printf("%d\n", g_var);
}

void __attribute__((destructor)) another_destructor() {
    g_var = g_var * 10 + 1;
    printf("%d\n", g_var);
}

int main() {
    printf("Main function\n");
    return g_var;
}
```

