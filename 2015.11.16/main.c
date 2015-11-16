#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a, b;
	float c, d;
	long e, f;
	unsigned int u, v;
	char c1, c2;
	scanf("%d %d", &a, &b);
	scanf("%f %f", &c, &d);
	scanf("%ld %ld", &e, &f);
	scanf("%o %o\n", &u, &v);
	scanf("%c %c", &c1, &c2);
	printf("a = %d, b = %d\n", a, b);
	printf("c = %.2f, d = %.2f\n", c, d);
	printf("e = %ld, f = %ld\n", e, f);
	printf("u = %o, v = %o\n", u, v);
	printf("c1 = %c, c2 = %c\n", c1, c2);
    return 0;
}
