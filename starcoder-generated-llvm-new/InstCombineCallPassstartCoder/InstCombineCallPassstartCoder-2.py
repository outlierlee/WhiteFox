
```cpp
const char const_str[] = "Hello, Wwworld!";

void example_function(char *dest) {
    memmove(dest, const_str, sizeof(const_str));
}

int main() {
    char buffer[50];
    example_function(buffer);
    return 0;
}
```

