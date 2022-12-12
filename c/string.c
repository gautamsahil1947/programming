#include <stdio.h>
const int maxinput = 100;
int main(void)
{
	char input[maxinput];
	printf("enter the string: ");
	scanf("%s", input);
	printf("you entered: %s\n", input);
	return 0;
}
