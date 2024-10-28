
```c
#include <stdio.h>

int main() {
    int result = 0; 
    int a = 1 << 31;
    int b = 18;
    int c = 25;
    
    for (int i = 0; i < 5; i++) {
        if (a > 0) {
            result += b;
        } 
        else {
            result -= c;
        }
    }
    
    if (result > 100) {
        result *= 2;
    } 
    else {
        result /= 2;
    }

    printf("%d", result);

    return result;
}
```
