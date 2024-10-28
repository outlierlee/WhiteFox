
```c
#include <stdio.h>

void loop_with_condition(int n, int flag) {
    int i = 0;
    while (i < n) {
        if (flag) {
            printf("Inside If loop Inside While loop\n");
            break;
        }
        printf("Outside If loop Inside While loop\n");
        i++;
    }
}

int main() {
    int n = 10;
    int flag = 1;

    loop_with_condition(n, flag);

    return 0;
}
```
