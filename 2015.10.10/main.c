#include <stdio.h>
#include <stdlib.h>

int main()
{
	double input;
	int loop_count = 7; //此处的数字越大计算越精确但是耗时更长，并且我使用了 int，意味着它不能大于 2147483648
	scanf("%lf", &input); // %lf 用来显示 double
	double output = 1;
	for (int i = 1; i <= loop_count; i++)
		output += pow(input, i) / factorial(i); // a += b 相当于 a = a + b，下面的 *= 同理
	printf("%lf", output);
	return 0;
}

int factorial(int i)
{
	int s = 1;
	for (int n = 1; n <= i; n ++) // 用 int n = 0 的话第一次循环就会变成乘以 0，后面就没有意义了，下同
		s *= n;
	return s;
}

double pow(double base, double sup) //power 乘方
{
	double sum = 1;
	for (double i = 1; i <= sup; i++)
		sum *= base;
	return sum;
}
