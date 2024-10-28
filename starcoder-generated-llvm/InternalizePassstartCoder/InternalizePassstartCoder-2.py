
```cpp
const int const_i = 10;
const float const_pi = 3.14;

void func1() {
    // Do something here
}

void func2() {
    // Do something here
}

int main() {
    volatile int i = const_i;
    volatile float pi = const_pi;
    func1();
    func2();
    return 0;
}
```
