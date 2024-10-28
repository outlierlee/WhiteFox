
```c
#include <stdio.h>

// Function will be unswitched due to loop and condition invariant
void loop_with_invariant(int n, const char *s) {
    const int slen = strlen(s);
    for (int i = 0; i < n; ++i) {
        if (s[i % slen]) {
            printf("%c ", s[i % slen]);
        }
    }
    printf("\n");
}

int main() {
    const char *some_string = "Hello World!";
    loop_with_invariant(20, some_string);

    return 0;
}
```

