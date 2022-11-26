/*
# include <stdio.h>
int main (void)
{
	int n;
	printf("enter the number: );
	scanf("%i" &n);
	printf("the number is: %i\n", n);
}
// the code above has a lot of bugs like the , in the line number 6 is missing
// and the second thing is that the "" are not in pair in the line number 5
*/
# include <stdio.h>
int main (void)
{
	// we want to  take a number input and print it.
	int n;
	printf("enter the number: ");
	scanf("%i", &n);
	printf("the number is: %i", n);



}
// this should work as intended.



















