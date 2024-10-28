
```c
#include <stdio.h>

void example_function(int a, int b) {
    for (int i = 0; i < a*b; i++) {
        for (int j = 0; j < a*b; j++) {
            if (i == j) {
                a++;
            } else {
                a--;
            }
        }
    }
    printf("%d\n", a);
}

int main() {
    example_function(10, 20);
    return 0;
}
```

