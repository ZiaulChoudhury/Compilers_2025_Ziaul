#include <stdio.h>

__attribute__((always_inline)) int fun(int x, int y)
{
	int z = x + y;
	return z ;
}

int main()
{
	int a, b;
	scanf("%d %d", &a, &b);
	printf(" %d ", fun(a,b));
	return 0;
}
