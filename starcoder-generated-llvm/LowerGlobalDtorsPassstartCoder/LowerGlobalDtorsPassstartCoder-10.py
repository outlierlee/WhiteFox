
```c
#include <stdio.h>

// Define a destructor function
void __attribute__((destructor)) my_destructor() {
    static int cnt = 0;
    printf("my_destructor called %d time(s)\n", ++cnt);
}

// Define another destructor function with a different priority
void __attribute__((destructor(101))) another_destructor() {
    static int cnt = 0;
    printf("another_destructor called %d time(s)\n", ++cnt);
}

int main() {
    printf("In main\n");
    return 0;
}
```
