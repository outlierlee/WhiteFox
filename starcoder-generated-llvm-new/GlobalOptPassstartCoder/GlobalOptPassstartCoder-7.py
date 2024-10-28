
```c
#include <string.h>

static int my_function(int a, int b) {
    int result = 0;
    if (a > b) {
        result = a * 2 + 15;
    } else {
        result = a + b - 15;
    }
    if (a > 100) {
        result = result - 15;
    } else {
        result = result * 2;
    }
    return result;
}

int main() {
    int x = (1 << 31);
    int y = 18;
    int main_result = my_function(x, y);
    return main_result;
}
```

