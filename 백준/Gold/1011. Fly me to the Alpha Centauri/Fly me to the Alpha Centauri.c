#include <stdio.h>
#include <math.h>

int count(int point1, int point2)
{
	int length = point2 - point1;
	int result, i;
	i = sqrt(length) + 1;
	if ((length - (i - 1) * (i - 2)) % (i - 1) == 0)
	{
		result = (i - 2) * 2 + (length - (i - 1) * (i - 2)) / (i - 1);
	}
	else if ((length - (i - 1) * (i - 2)) % (i - 1) != 0)
	{
		result = (i - 2) * 2 + (length - (i - 1) * (i - 2)) / (i - 1) + 1;
	}
	return result;
}

int main(void)
{
	int testcase, point1, point2;
	scanf("%d", &testcase);
	for (int i = 0; i < testcase; i++)
	{
		scanf("%d %d", &point1, &point2);
		printf("%d\n", count(point1, point2));
	}
	return 0;
}