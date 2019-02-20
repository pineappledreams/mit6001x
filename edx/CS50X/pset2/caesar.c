#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>

int main(int argc, char *argv[])
{

    // Print error message if too much or little info is given. Exit program.
    if (argc != 2)
    {
        printf("Please enter only ONE (1) number when running for the cipher key.\n");
        return 1;
    }

    // Save the key value into k. Also if it's some ridiculously big number, it will just modulo the crap outta it.
    int k = atoi(argv[1]);
    k = k % 26;

    printf("Your key is: %i\n", k);

    // Accept text input here.

    string plaintext = get_string("plaintext: ");

    // ensure string was read, quit if nothing was inserted.
    if (plaintext == NULL)
    {
        return 1;
    }

    printf("plaintext: %s", plaintext);

    // Apply cipher here.
    // First we check if it's alphanumeric, then we will apply the cipher.
    // UPPER RANGE: 65 - 90, lower range: 97 - 122 (25 for each...)

    string ciphertext;
    ciphertext = plaintext;

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (isupper(plaintext[i]))
            {
                ciphertext[i] = ((((plaintext[i] - 65) + k) % 26) + 65);
            }
            else
            {
                ciphertext[i] = ((((plaintext[i] - 97) + k) % 26) + 97);
            }
        }
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }

    // Print out the ciphertext, print newline, exit.

    printf(" ciphertext: %s", ciphertext);
    printf("\n");
    return 0;

}