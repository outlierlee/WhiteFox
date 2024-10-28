
```c
#include <stdio.h>

// Declare a function that accepts several parameters
int varargs_func(int x, int y, float z, char str_char) {
    int result = x * 10 + y;
    if(str_char == 'a' && z > 5.5) {
        result = result + 2;
    }
    else {
        result = result - 2;
    }
    return result * 2;
}

int main() {
    int result;
    int a = 0x55555555;
    int b = 10;  
    float c = 12.3452;
    char d = 'a';

    // Call the function with different types of parameters
    result = varargs_func(a, b, c, d);
    printf("Result: %d\n", result);

    result = varargs_func(123, 456, 7.89, 'b');
    printf("Result: %d\n", result);

    return 0;
}
```

