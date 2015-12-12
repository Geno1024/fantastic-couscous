#include<stdio.h>
#define row 10
int main(void)
{
	int i,j;
	int a[10][19];
	for(i=1;i<=10;i++)
	{
		for(i=1;i<=10;i++)
		{
			a[i][11-i]=1;
			a[i][9+i]=1;
		}
		for(i=2;i<=10;i++)
		{
			for(j=1;j<=19;j++)
			{a[i][j]=a[i-1][j-1]+a[i-1][j+1];}
		}	
		for(i=1;i<=10;i++)
		{
			for(j=1;j<=19;j++)
			{
				if(a[i][j]!=0)
				printf("%2d",a[i][j]);
				else
				printf(" ");
			}
			printf("\n");
		}
	}
	//getch();
	return 0;		
}