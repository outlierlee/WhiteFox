
```cpp
int func(int x, int y) {
    return x + y;
}

int main() {
    int x = 18;
    int y = 25;
    int result = func(x, y);
    short truncated_result = static_cast<short>(result);
    return truncated_result;
}
```

