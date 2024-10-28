
```cpp
int main() {
    int x = 0; // declare and initialize a variable
    int y = 1; // declare and initialize another variable

    // A simple conditional structure that creates a unreachable block
    if (x < y) {
        // This block is unreachable because x is not less than y
        printf("Unreachable block\n");
    } else {
        // This block is reachable
        printf("Reachable block\n");
    }

    // A loop that never executes, creating another unreachable block
    while (x < y) {
        printf("Unreachable loop block\n");
    }

    return 0;
}
```

