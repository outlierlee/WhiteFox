
```c
#include <stdio.h>

#define N 5

char buff[N];
char* ptr;

char func() {
    ptr = "Hello w";

    for (int i=0; i < 5; i++) {
        *(ptr + 3) = 0;
    }
    return  *ptr;
}

int main() {
    char result = func();
    return 0;
}
```

