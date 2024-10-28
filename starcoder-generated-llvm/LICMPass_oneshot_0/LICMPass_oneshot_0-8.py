
```cpp
int no_side_effect_func(int x) {
    if (x <= 5) {
        return x * 5;
    } else {
        return x / 2;
    }
}

int main() {
    int x = 10;
    int result = 0;
    for (int i = 0; i < 5; ++i) {
        int temp = x * i;
        int scream = no_side_effect_func(temp);
        if (scream > 100) {
            result = scream;
            break;
        }
    }
    return result;
}
```

