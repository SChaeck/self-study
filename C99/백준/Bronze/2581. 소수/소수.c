#include <stdio.h>

int prime_num_check(int num)
{
	if (num == 1)
		return 0;
	for (int i = 2; i <= num; i++)
	{
		if (i == num)
			return 1;
		else if (num % i == 0)
			return 0;
	}
}

int main(void)
{
	int num1, num2, sum = 0, min = -1;
	scanf("%d %d", &num1, &num2);
	for (int i = num2; i >= num1; i--)
	{
		if (prime_num_check(i) == 1)
		{
			min = i;
			sum += i;
		}
	}
	if (sum != 0)
		printf("%d\n", sum);
	printf("%d", min);
	return 0;
}