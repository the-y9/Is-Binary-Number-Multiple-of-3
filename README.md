# Is-Binary-Number-Multiple-of-3
The Solution class is defined. This class contains a single method isDivisible which takes a string s as input and returns either 1 or 0 based on whether the binary representation of s is divisible by 3.

Inside the isDivisible method, the binary string s is converted to its decimal representation using the int() function and the base value of 2. The int(s, 2) converts the binary string to decimal.

The decimal value obtained from step 2 is then checked if it is divisible by 3 using the modulo operator %. If the decimal value is divisible by 3 (i.e., int(s, 2) % 3 == 0), the method returns 1. Otherwise, it returns 0.

In the main code section, the number of test cases T is taken as input.

For each test case, a binary string s is taken as input.

An instance of the Solution class is created with ob = Solution().

The isDivisible method is called on the ob instance with s as the argument, and the result is stored in the variable ans.

Finally, the value of ans is printed.

Overall, this code checks whether the binary representation of each input string is divisible by 3 and prints 1 if it is divisible and 0 otherwise.
