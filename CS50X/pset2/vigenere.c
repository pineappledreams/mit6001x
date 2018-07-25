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
    else
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (!isalpha(argv[1][i]))
            {
                printf("I spent an hour finding how to remove alphanums.\n40 pages and 0 solutions.\nPlease clap!\n");
                return 1;
            }
        }
    }


    // Save the key value into k. Makes it upper for the ciphering.
    string k = argv[1];
    for (int i = 0, n = strlen(k); i < n; i++)
    {
        k[i] = toupper(k[i]);
    }

    //printf("Your key is: %s\n", k);

    // Accept text input here.

    string plaintext = get_string("plaintext: ");

    // ensure string was read, quit if nothing was inserted.
    if (plaintext == NULL)
    {
        return 1;
    }

    // Apply cipher here.
    // First we check if it's alphanumeric, then we will apply the cipher.
    // UPPER RANGE: 65 - 90, lower range: 97 - 122 (25 for each...)

    //initialize loop for strlen - we will need it when we will have a short keyword but a long string to encrypt.
    //Every time it runs, it should modulo the index - if the index is too big, then it will modulo and start again
    //from the beginning of the keyword.

    int loop = strlen(k);

    //garbage keeps count of nonalphanumberic chars inside the plaintext so that we will shift the i of the cipher
    //ONLY when we encrypt an alphanumeric char.

    int garbage = 0;

    string ciphertext;
    ciphertext = plaintext;

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (isupper(plaintext[i]))
            {
                ciphertext[i] = ((((plaintext[i] - 65) + (k[(i - garbage) % loop] - 65)) % 26) + 65);
            }
            else
            {
                ciphertext[i] = ((((plaintext[i] - 97) + (k[(i - garbage) % loop] - 65)) % 26) + 97);
            }
        }
        else
        {
            ciphertext[i] = plaintext[i];
            garbage++;
        }
    }

    // Print out the ciphertext, print newline, exit.

    printf("ciphertext: %s", ciphertext);
    printf("\n");
    return 0;

}