
```c
#include <stdio.h>

void loop_with_condition(int n, int flag) {
	for (int i = 0; i < n; ++i) {
		if (flag) {
			printf("%d ", i * 2);
		} else {
			printf("%d ", i * i);
		}
	}
	printf("\n");
}

int main() {
	int n = 15, flag = 1;
	loop_with_condition(n, flag);
	return 0;
}
```

