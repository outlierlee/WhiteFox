
```cpp
void loop_func(int x) {
    for (int i = 0; i < x; ++i) {
        if (i % 2) {
            printf("%d ", i);
        } else {
            printf("%d ", -i);
        }
    }
}

int main() {
    int x = 10;
    loop_func(x);
    return 0;
}
```

