
```cpp
#include<iostream>

int simple_conditional(int a, int b, int c, int d) {
   return a + b - c + d;
}

int main() {
    int x = 10;
    int y = 20;
    int z = x / 5;
    int w = x * 2;
    int result = simple_conditional(x + 3, y - z, w, z);
    if (result > 50){
        std::cout<<"Result is greater than 50\n";
    }
    else{
        std::cout<<"Result is 50 or less\n";
    }
    return 0;
}
```
