#include <stdio.h>

int main(void)
{
	int x, y, w, h;
	scanf("%d %d %d %d",&x,&y,&w,&h);
	int small_x = x <= (w-x) ? x : (w-x);
	int small_y = y <= (h-y) ? y : (h-y);
	if(small_x <= small_y)
		printf("%d",small_x);
	else
		printf("%d",small_y);
	return 0;
}