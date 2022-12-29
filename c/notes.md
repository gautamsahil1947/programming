
## [Algorithms](https://cs50.harvard.edu/x/2022/notes/0/#algorithms)

-   Now that we can represent inputs and outputs, we can work on problem solving. The black box that transforms inputs to outputs contains **algorithms**, step-by-step instructions for solving problems:  
    ![box with word "algorithms"](https://cs50.harvard.edu/x/2022/notes/0/algorithms.png)
-   We might have an application on our phones that store our contacts, with their names and phone numbers sorted alphabetically. The old-school equivalent might be a phone book, a printed copy of names and phone numbers.
-   We might open the book and start from the first page, looking for a name one page at a time. This algorithm would be correct, since we will eventually find the name if it’s in the book.
-   We might flip through the book two pages at a time, but this algorithm will not be correct since we might skip the page with our name on it.
-   Another algorithm would be opening the phone book to the middle, decide whether our name will be in the left half or right half of the book (because the book is alphabetized), and reduce the size of our problem by half. We can repeat this until we find our name, dividing the problem in half each time.
-   We can visualize the efficiency of each of those algorithms with a chart:  
    ![chart with: "size of problem" as x-axis; "time to solve" as y-axis; red, steep straight line from origin to top of graph labeled "n"; yellow, less steep straight line from origin to top of graph labeled "n/2"; green, curved line that gets less and less steep from origin to right of graph labeled "log_2  n"](https://cs50.harvard.edu/x/2022/notes/0/time_to_solve.png)
    -   Our first algorithm, searching one page at a time, can be represented by the red line: our time to solve increases linearly as the size of the problem increases. _n_ is a number representing the size of the problem, so with _n_ pages in our phone books, we have to take up to _n_ steps to find a name.
    -   The second algorithm, searching two pages at a time, can be represented by the yellow line: our slope is less steep, but still linear. Now, we only need (roughly) _n_ / 2 steps, since we flip two pages at a time.
    -   Our final algorithm, dividing the phone book in half each time, can be represented by the green line, with a fundamentally different relationship between the size of the problem and the time to solve it. If the phone book doubled in size from 1000 to 2000 pages, we would only need one more step to find our name.

## [Pseudocode](https://cs50.harvard.edu/x/2022/notes/0/#pseudocode)

-   We can write **pseudocode**, which is a representation of our algorithm in precise English (or some other human language):
    
    ```
    1  Pick up phone book
    2  Open to middle of phone book
    3  Look at page
    4  If person is on page
    5      Call person
    6  Else if person is earlier in book
    7      Open to middle of left half of book
    8      Go back to line 3
    9  Else if person is later in book
    10     Open to middle of right half of book
    11     Go back to line 3
    12 Else
    13     Quit
    
    ```
    
    -   With these steps, we check the middle page, decide what to do, and repeat. If the person isn’t on the page, and there’s no more pages in the book left, then we stop. And that final case is particularly important to remember. When programs or code don’t include that final case, they might appear to freeze or stop responding, or continue to repeat the same work over and over without making any progress.
-   Some of these lines start with actions or verbs that solve a smaller problem. We’ll start calling these _functions_:
    
    ```
    1  Pick up phone book
    2  Open to middle of phone book
    3  Look at page
    4  If person is on page
    5      Call person
    6  Else if person is earlier in book
    7      Open to middle of left half of book
    8      Go back to line 3
    9  Else if person is later in book
    10     Open to middle of right half of book
    11     Go back to line 3
    12 Else
    13     Quit
    
    ```
    
-   We also have branches that lead to different paths, like forks in the road, which we’ll call _conditionals_:
    
    ```
    1  Pick up phone book
    2  Open to middle of phone book
    3  Look at page
    4  If person is on page
    5      Call person
    6  Else if person is earlier in book
    7      Open to middle of left half of book
    8      Go back to line 3
    9  Else if person is later in book
    10     Open to middle of right half of book
    11     Go back to line 3
    12 Else
    13     Quit
    
    ```
    
-   And the questions that decide where we go are called _Boolean expressions_, which eventually result in answers of yes or no, or true or false:
    
    ```
    1  Pick up phone book
    2  Open to middle of phone book
    3  Look at page
    4  If person is on page
    5      Call person
    6  Else if person is earlier in book
    7      Open to middle of left half of book
    8      Go back to line 3
    9  Else if person is later in book
    10     Open to middle of right half of book
    11     Go back to line 3
    12 Else
    13     Quit
    
    ```
    
-   Lastly, we have words that create cycles, where we can repeat parts of our program, called _loops_:
    
    ```
    1  Pick up phone book
    2  Open to middle of phone book
    3  Look at page
    4  If person is on page
    5      Call person
    6  Else if person is earlier in book
    7      Open to middle of left half of book
    8      Go back to line 3
    9  Else if person is later in book
    10     Open to middle of right half of book
    11     Go back to line 3
    12 Else
    13     Quit
    
    ```
    
-   We’ll soon encounter other ideas, too:
    -   functions
        -   arguments, return values
    -   conditionals
    -   Boolean expressions
    -   loops
    -   variables
    -   …
-   And David’s first program just printed “hello, world” to the screen:
    
    ```c
    #include <stdio.h>
    
    int main(void)
    {
        printf("hello, world\n");
    }
    ```
    
    -   But this program, written in a language called C, has lots of other syntax that keeps us from focusing on these core ideas.
--- 
## C language
- your code needs to be
  - correct
  - well designed
  - styled well

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```
- this code prints hello, world. well what after writing a code. how will a computer understand those words or sentences.
- a computer only understands binary language (0's and 1's) and to convert a code from text to (0's and 1's), we need a programm called compiler. a compiler converts text/ code to (0's and 1's) which a machine can understand.
- c files have an extension (.c) like hello.c and points.c

- `make hello` is a command to compile a file named hello.c and gives out an executable file. you can run that executable file using the command `./hello` 

```c 
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```
- if you compile and run this program, it prints hello, world. 
```c 
#include <stdio.h>

int main(void)
{
    printf("hello, there\n");
}
```
- this also prints hello, world inspite of the changes made. this is because in order to make those changes reflect, we have to recompile the file. 
- `make` itself is not a compiler, it knows how to find the compiler and use it on the system and give the compiled file.

### Functions in C
- functions are actions or verbs like say or print which are used to do certain specific tasks. functions take inputs otherwise called arguments.
```c
printf("hello, world"); 
```
- printf is a function in c. 'f' in printf stands for formatted, it takes all the inputs in the `""` double quotes and a `;` semicolon at the end.
the semicolon at the end is similar to the fullstop in english for finishing the thought.

- some functions have visual side effects like the printf function, but there are funcions which hand you back some reutrn values which you can use and reuse again.
- in C if you have a word followed by open and close parenthesis, it is most likely a function with a few exceptions
```c
string answer = get_strint("what is your name? ");
```
- `get_string` is a function which displays the prompt message between the `""` to the user and stores whatever the user types over to the left in the variable named `answer` 
- in C, in order to declare a variable, you also have to tell about the data type of the variable `string` in this case.
- `= ` is called the assignment operator and used to copy values from right to left.

```c
...
printf("hello, world\n");
...
```
- the output is 
```
$ make hello
$ ./hello
hello, world
$ 
```
- but if the   `\n` character is removed, then the output becomes
```
$ make hello
$ ./hello
hello, world$
```
- therefore we can conclude that `\n` is some way of telling the computer that after the execution of this line, start with a new line. it is called **escape sequence** or a **newline character**.
```c
printf("hello,world
 ");
```
- this pops an error for according to the set rules, the double quotes `""` should be in the same line.
- let's try taking input and greating the user with hello, user_name in this case
```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // get_string function is in cs50 library
    string answer = get_string("what is your name? ");
    // trying to print the message
    printf("hello, answer\n");
}
```
- this prints `hello, answer` on the terminal. so for printing hello, sahil in my case, i have to use something called place holders to tell the compiler to insert the value of a certain variable at certain place.
```c
...
printf("hello, %s\n", answer);
...
```
- `%s` is a place holder (FORMAT CODE) which is used to place a string at its place. 
- we also need to provide the variable which holdes the string after the `""` , _answer_ in this case
- some functions come with the language and for those which do not come with it, we have to use libraries. so the `#include <stdio.h>` is inclucing the functionalities of the standard input and output library, for example `printf`, `scanf` etc.

- similarly to use the function `get_string`, we have to use the cs50 library.

- `%s` means 'hi computer, replace this %s with a string eventually'. and the f in printf means formatted, therefore printf does all that formatting or placing the strings in place of %s

- another approach to this question 
```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // this thing also wroks
    printf("hello, %s\n", get_string("what is your name? "));
}
```
- but this is worth it if you want to use the name only once. Reusability is being compromised.

```c
int main(void)
{
    // this is the core of your programm
}
```
- executing a code in C, fires up the main function.
this function has it all.

```c
#include <stdio.h>
#include <cs50.h>
```
- `stdio.h` is a header file for the standard input output library and contains a menu of functions like `printf` , `scanf` etc. and it prepares the compiler on how these functions are implemented.

- the functions are in the `stdio.c`,  `cs50.c` files and provide all the functionality and the `#include` is the specific mechanism to use it, via header files.

### Some Linux Commands
- `pwd` &rarr; is used to print the directory in which you are right now. it stands for _present working directory._
- `ls` &rarr; is used to list the contents of a directory. 
  - `ls -a` &rarr; is used to list all the contenst of a directory including the _hidden files_
- `cd` &rarr;  is used to change directories. 
  - `cd ..` &rarr; is used to get out of the `pwd` into the parent directory.
  - `cd ../..` &rarr; is used to go to the grand parent directory, which is parent 
  directory of the parent directory.
  - `cd abcd` &rarr; is used to go into a directory inside the pwd, named *abcd*.
- `mkdir abcd` &rarr; is used to create an empty directory inside the `pwd` named *abcd*
- `rmdir abcd` &rarr; is used to remove a directory in `pwd` named *abcd*. But this removes only an empty directory
- `cp hello.c sahil.c` &rarr; is used to make a copy of a file. in this case a copy of **hello.c** is made and is named **sahil.c**
- `mv hello.c ../../sahil` &rarr; is used to **rename** or **move** a file. in this case hello.c is moved to a directory named sahil in the grandparent directory.
- `rm abcd` &rarr; is used to remove a file in the pwd named *abcd*. But there pops a comfirmation message.
  - `rm -f abcd` &rarr; here `-f` means forcefully. it just deletes the file named *abcd*
  - `rm -r abcd` &rarr; is used to delete a directory named abcd. here the `-r` flag means recursively remove. but this also asks for confirmation message 
  - `rm -rf abcd` &rarr; means remove the directory named abcd recursively and forcefully.

- if `..` refers to parent and `../..` refers to the grand parent, then `.` refers to the present directory


- `bool`, `char %c`, `int %i`, `long %li`, `float %f`, `double %f`, `string %s` are some of the data types in c and their format codes
- `get_char`, `get_int`, `get_long`, `get_float`, `get_double`, `get_string` are some of the functions from CS50 library corresponding to taking input of the data types.

- `+`, `-`, `*`, `/`, `%` are some of the operators in c.

```c
...
// to count 
int counter = 0; // initiation point
...
... 
counter = counter + 1; // increment
...
```
- this can also be represented in short hand notation called `syntactic sugar`
- once the data type of the variable is declared, you don't need to mention it again and again.
```c
int counter = 0;
...
...
counter = counter + 1;
counter += 1;
counter++;

// or 
counter = counter - 1;
counter -= 1;
counter--;
// represent the same thing adding 1 and subtracting one
```
- the `=` used here is assignment operator, so first the expression on the right hand side is calculated and then the answer is assigned to the variable on the left hand side.

> let's make a calculator which asks the user for inputs and prints the sum .
```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");
    // printf(x + y); this is not the way it works (why?)
    printf("%i\n", x + y);
}
```
- the first argument in printf has to be a string in double quotes.
```c
int z = x + y;
printf("%i\n", z);
```
- if the sum is to be used and reused again and again, then it is better to use z as a container for sum.
- pressing  `tab` on the command line completes what you were typing
- using &uarr; and &darr; you can nevigate through all the commands that were executed on the terminal.
```
$ make calculator 
$ ./calculator
x: 1000000000
y: 1000000000
2000000000
$ ./calculator
x: 2000000000
y: 2000000000
-294967296
$ 
```
- this is because the integer ran out of bits. an `int` uses `32 bits` or `4 bytes`. with 8 bytes, you can count as high as 256. with 32 bits, you can count about 4 billion. but since integer also consists of negative integers, so the  max we can count with an integer is roughly 2 billion in both the directions.
- the temperary solution for this problem is to use `long int` instead of `int`. but this does not slove the problem and just pushes the can further down the street...
### Conditionals
```c
...
if (condition)
{
    // the code inside
}
...
```
-  if is not a function. it is a feature of the C language. if the condition inside is true, then the block of if is executed, else the if block is skipped and the code after it is executed
```c
if (condition)
{
    // code 1
}
else
{
    // code 2
}
```
- in case of if-else ladder, if the condition is true, then the if block is executed and the else is ignored. but if the condition is false, then the else block is executed and the if block is ignored.
```c
if (condition 1)
{
    // code 1
}
else if (condition 2)
{
    // code 2
}
else
{
    // code 3
}
```
- if the if condition is correct, then all else-if and else are ignored. 
- in case of if-else-if-else ladder,  block with the first correct condition is executed and rest are ignored. if no condition was correct, then the else block is executed (if any).
- onle one block will be executed in a if-elseif-else ladder or if-else ladder
- you can use multiple ifs if all the conditions are independent of each other.
- we do not use the semicolon after the conditionals

> lets write a simple programm taht prompts user for marks lost and then compares those marks to your marks. (points.c)
```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int points = get_int("how many points did you loose? ");
    
    if (points < 2)
    {
        printf("you lost fewer points than me\n");
    }
    else if (points > 2)
    {
        printf("you lost more points than me\n");
    }
    else if (points == 2)
    {
        printf("you lost same points as me\n");
    }

}
```
- the last line is not required as we do not need to ask three questions when the third one is obvious
```c
...
...
// no need to use else if again 
else 
{
    printf("you lost same points as me\n");
}
```
- there is still a bit redundency in the code. the number **2** also refered as the `magic number`, repeats two times and is manually hard coded. if in future it has to be changed, then it will be tedious and also induces probability of screwing up at some point of time.
- so we can declare a variable for my marks
```c
int mine = 2;
```
- and since we don't want to change this constant accidently, we should declare the variable a `constant` using the `const` keyword.
- the constant variables are written in capitals, not by convention, but for the sake of awareness, that it is a constant
```c
const int MINE = 2;
```
> write a code to take a number from the user and print whether it is even or odd (parity.c)
```c
#include <stdio.h>
#include <cs50.h>
 
int main(void)
{
    int n = get_int("n: ");
    
    // if n is even
    if (n % 2 == 0)
    {
        printf("even\n");
    } 
    else
    {
        printf("odd\n");
    }

}
```
- here the `==` is the equality operator and is used to compare two values
- `%` is called the remainder operator and is used to find the remainder 
 ```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char c = get_char("agreed or not agreed? ");

    if (c == 'y')
    {
        printf("agreed\n");
    }
    else if (c == 'n')
    {
        printf("not agreed\n");
    }
}
 ```
- this does not accomodate the possibilities of 'Y' and 'N'. 

- **as soon as you find yourself copy pasting, you are probably doing something wrong**
```c
// (c == 'y' or c == 'Y')
if (c == 'y' || c == 'Y')
{
    // this is how c accomodates logical or
}
```
- similarly the logical and becomes
```c
// (a % 2 == 0 and a < 55)
if (a % 2 == 0 && a < 55)
{
    // this is how c accomodates logical and
}
```
- so the code becomes
 ```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char c = get_char("agreed or not agreed? ");

    if (c == 'y' || c == 'Y')
    {
        printf("agreed\n");
    }
    else if (c == 'n' || c == 'N')
    {
        printf("not agreed\n");
    }
}
 ```
 - `||` stands for logical OR, `&&` stands for logical AND, `==` is an equality operator
 - all the questions in the conditionals has to be explisit
 ```c
 if (c == 'y' || 'Y')
//  this is not a valid condition
 ```
 - chars use `' '` single quotes and strings use double quotes even for single character.
 - you cannot compare strings directly as you do with chars. to compare strings, there is a function in the `string.c` library `strcmp` which returns 0 if the strings are same.
 ```c
#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
   string c = get_string("agreed or not agreed? ");

   if (strcmp(c, "y") == 0 || strcmp(c, "Y") == 0)
   {
       printf("agreed\n");
   }
   else if (strcmp(c, "n") == 0 || strcmp(c, "N") == 0)
   {
       printf("not agreed\n");
   }
}
 ```
 - if there is `0` inside the if conditional, it is considered `false`. similarly if `anything except 0` is inside the conditional, it is considered `true` by default.
 - alternate way to do this 
 ```c
#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
   string c = get_string("agreed or not agreed? ");

   if (!strcmp(c, "y") || !strcmp(c, "Y"))
   {
       printf("agreed\n");
   }
   else if (!strcmp(c, "n") || !strcmp(c, "N"))
   {
       printf("not agreed\n");
   }
}
 ```
 - `!` is the not operator and inverts the sense of a statement.
   - `!true` &rarr; false
   - `!false` &rarr; true
   - `!0` &rarr; 1 (true)
   - `!1` &rarr; 0 (false)

> write a code to print meow three times (meow.c)
```c
#include <stdio.h>

int main(void)
{
    printf("meow\n");
    printf("meow\n");
    printf("meow\n");
}
```
- this thing works, but there should be a better way to do it instead of copying and pasting.
### Loops in C
 - forever loop in C
 ```c
while (true)
{
    // while block
}
 ```
- while loop takes boolean expression in the (parantheses) and any condition which is true will work here, like `2 < 3` and so on. therefore using `true` makes it clear in the long run. `false` here means false. you can also use 0 for false and 1 for true.

- if you want to implement a loop for certain number of times, this is how you do it
```c
int n = get_int("how many times? ");

int counter = 0;
while (counter < n)
{
    printf("meow\n");
    counter++;
}
```
- the code above is to implement the physicallity of counting upwards in code
> dry running the code above for better understanding
> - n = 3 input from the user
> - counter = 0
> - check the while condition 0 < 3
>   - print meow 
>   - increase counter by 1 &rarr; counter = 1
> - check the while condition 1 < 3 
>   - print meow 
>   - increase counter by 1 &rarr; counter = 2
> - check the while condition 2 < 3
>   - print meow 
>   - increase counter by 1 &rarr; counter = 3
> - check the while condition 3 < 3
>   - the condition is false
>   - skip the while block and move further in the code (if any)
- if you want to count `n` times, you can either count from `0 to n - 1` or `1 to n`
- the code above can be tightened up as follows
```c
int n = get_int("how many times? ");

int i = 0; // initialising counter variable to baseline 0
while (i < n)
{
    printf("meow\n");
    i++; // increment logic
}
```
- or this also does the same thing just the counting differs.
```c
int n = get_int("how many times? ");

int i = 1; // initialising counter variable to baseline 0
while (i <= n)
{
    printf("meow\n");
    i++; // increment logic
}
```
- same thing can be done with for loop in c
```c
int n = get_int("how many times? ");
for (int i = 0; i < n; i++)
{
    // the block of for loop
}
```
> in for loop, 
> - the first segment initialises the counter variable
> - the second segment is the condition 
> - the third one is the increment or decrement

> how does a for loop work?
> - first it initiates the variable> - for loops are used where we have to count finite number of times 
> - then it checks the condition. 
>   - if the condition is true, the code is executed, else the for block is skipped
> - then the last segment is executed that is the increment or decrement
> - again the condition is checked. this goes on till the condition turns false.

> what is the difference between for loop and  while loop?
> - for loop and while loops can be used to do the same things. the only difference comes in the scope of the variables declared.
> - in case of the while loop, the variable is declared outside the while block, so can be accessed anywhere in the code, whereas the variable of the for loop is available inside the loop only.

- the increment logic inside the for loop need not be the `i++` or `i--`, it can be any valid logic for change in variable.
```c
#include <stdio.h>
#include <cs50.h>
#include <string.h>


int main(void)
{
    for (int i = 1; i < 555; i = i*2)
    {
        printf("%i\n", i);
    }
}
// for (variable initiation; condition; loop progression condition)
```
- you can initiate more than one variables of same data type inside the for loop variable initiation
```c
for (int i = 0, j = 6; i < j; i++)
{
    // code to be executed
}
```
- let's use loops to improve the design of the code we wrote (meow.c)
```c
#include <stdio.h>

int main(void)
{
   for (int i = 0; i < 3; i++)
   {
        printf("meow\n");
   }
}
```
```
$ make meow 
$ ./meow 
meow
meow
meow
$ 
```
### Abstraction
- now we have a piece of code which does meowing. let's make our own custom function meow
```c
output name(input)
{
    // code of the function
}
```
- the function should be defined outside the main function on the top as the compiler reads the code top to bottom.
- void is used to say no explicitly


```c
#include <stdio.h>
// defining a function meow
void meow(void)
{
    printf("meow\n");
}

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        // calling the function meow
        meow();
    }
}
```
- so now the function meow exists, if we move it way down in the code, the compiler throws an error, as it reads the code top to bottom and the function is called before defining it.
- to solve this, a prototype  of the function is placed above main to let the compiler know that a funciton exists
```c
#include <stdio.h>
// prototype of our function
void meow(void);

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        // calling the function meow
        meow();
    }
}



// defining a function meow
void meow(void)
{
    printf("meow\n");
}
```
- it can be improved further
```c
#include <stdio.h>
// prototype of our function
void meow(int j);

int main(void)
{
    // calling the function meow
    meow(3);
}



// defining a function meow
void meow(int j)
{
    
    for (int i = 0, n = j; i < n; i++)
    {
        printf("meow\n"); 
    }
}
```
- when making modifications to the functions, do not forget to change the prototype 
- similar to our prototypes, the header files like `stdio.h` and `cs50.h` have a menu of header files so as to prepare the compiler on how these functions are implemented or what functions to expect

>let's code a programm to discount some prices (discount.c)
```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float regular = get_float("regular? ");
    float sale = regular * .85;
    printf("sale price : %.2f\n", sale);
}
```
- this can be improved further by declaring a function that does all the discount
```c
#include <stdio.h>
#include <cs50.h>

float discount(float p);

int main(void)
{
    float regular = get_float("regular? ");
    float sale = discount(regular);
    printf("sale price : %.2f\n", sale);
}


float discount(float p)
{
    // p = p * .85;
    // return p;
    // // or
    return p * .85;
}
```
- return in the function discount is returning or handing back the value to be stored and reused.
- functions in c can take multiple arguments.
> write a programm improving discount.c, taking price and % discount and printing the sale price
```c
#include <stdio.h>
#include <cs50.h>

float discount(float cost, float off);

int main(void)
{
    float price = get_float("price: ");
    float percentage_off = get_float("percentage off: ");
    float sale = discount(price, percentage_off);
    printf("sale price %.2f\n", sale);
}

float discount(float cost, float off)
{
    return cost * (100 - off)/100;
}
```
### scope of a variable
- a variable defined inside main function is limited to the main function.
- variables like cost and off are scoped inside the function discount only and are not accessible outside
- changing `cost` does not affect the `price` variable as cost is a copy of price and changing a copy does not change the orignal one.
### ascii art
```c
#include <stdio.h>

int main(void)
{
    printf("####\n");
}
```
```c
#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 4; i++)
    {
        // print four brics in a line
        printf("#");
    }
    // after printing, move to the next line
    printf("\n");
}
```
- both the codes give the same result
```
$ make test 
$ ./test
####
$ 

```
### Do - While loop in C
```c
int n;
do
{
    // the block to be executed
}
while (condition);
```
- a `do - while` loop is used when you want to run a code atleast once and then check the condition. 
- it is synonymous to _"do the following, while true"_. therefore the do while loop breaks as soon as the condition is false.

> write a code to print the following structure of the width given by the user.
```
size: 3
###
###
###
```

```c
#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int i;
    do
    {
        i = get_int("size: ");
    }
    while ( i < 1);
    // for each row
    for (int j = 0; j < i; j++)
    {
        // for each column
        for (int k = 0; k < i; k++)
        {
            // print a brick
            printf("#");
        }
        // move to the next line
        printf("\n");
    }
}
```
```
$ make test 
$ ./test
size: -8
size: -7
size: 
size: 0
size: 
size: 2
##
##
$ 
```

.
.
.
.
.
.
.
.
. left for future













