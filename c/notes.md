
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



































