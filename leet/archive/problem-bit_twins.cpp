Bit-Twins
Programming challenge description:

Summary:

Count bit twins in a 32bit number

Description:

Write a program that, given a decimal number represented as a string, prints
the number of bit-twins found within the 32bit binary representation of that
number.

A bit-twin is a sequence of two bits which are 1 surrounded by two bits which
are 0 (ie. bit pattern 0110 represents a bit-twin).

Note: In any doubt, write your assumptions as comments. If you experience
issues with the tool or the language, a pseudo-code describing your algorithm
is acceptable.
Input:

Your program should read lines from the standard input. Each line contains a
string number. For example

6

1610612736
Output:

For each input number print to the standard output the number of bit twins. For
example, for the input above:

1

1
Test 1
Test Input
6
Expected Output
1
Test 2
Test Input
1610612736
Expected Output
1

#include <stdio.h>
#include <stdlib.h>

int main() {
  const size_t maxLineLen = 1024;
  char line [maxLineLen];

  while(fgets(line, maxLineLen, stdin) != NULL) {
    // Making an assumption that the 32 bit number is a long int with base 10
    long int val = strtol(line, NULL, 10);

    // Iterate through the binary representation starting
    // from the most significant bit to the least significant bit.
    // We are assuming the number is a 32-bit integer
    int num_twins = 0;
    int num_ones = 0;
    for (int i = 31; i >= 0; i--) {
      const int mask = 1 << i;
      const int bit = (val & mask) >> i;
      num_ones += bit;

      // Traversing left to right when we ecounter a zero bit, and num_ones == 2 add to
      // total number of binary twins, else reset number of ones.
      if (bit == 0) {
        if (num_ones == 2) {
          num_twins++;
        }
        num_ones = 0;
      }
    }

    // At the end of the traversal if we have two 1's at the end
    // add that to the total number of twins (e.g. 0011)
    if (num_ones == 2) {
      num_twins++;
    }

    printf("%d", num_twins);
  }

  return 0;
}
