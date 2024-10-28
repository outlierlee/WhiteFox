
```c
#include <stdio.h>

void loop_with_condition(int n, int flag) {
    for (int i = 0; i < n; ++i) {
        if (flag) {
            printf("Flag is true, iteration %d\n", i);
        } else {
            printf("Flag is false, iteration %d\n", i);
        }
    }
}

int main() {
    int n = 10;
    int flag = 1;

    loop_with_condition(n, flag);

    return 0;
}
```

