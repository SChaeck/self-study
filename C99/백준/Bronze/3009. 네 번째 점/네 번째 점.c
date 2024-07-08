#include <stdio.h>

int check(int x[])
{
	if(x[0] != x[1] && x[0] != x[2])
		return (x[0]);
	else if(x[1] != x[0] && x[1] != x[2])
		return (x[1]);
	else
		return (x[2]);
}

int main(void)
{
	int x[3], y[3];
	int x4, y4;
	for(int i = 0; i < 3; i++)
	{
		scanf("%d %d",&x[i],&y[i]);
	}
	x4 = check(x);
	y4 = check(y);
	printf("%d %d",x4,y4);
	return 0;
}