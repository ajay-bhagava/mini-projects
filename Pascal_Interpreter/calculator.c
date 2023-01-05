#include <stdio.h>
#include <stdlib.h>

#define INTEGER "integer"
#define PLUS "plus"
#define MINUS "minus"

struct Token {
    int value;
    char type[8]
};

struct Token generateToken(char *text, int index) 
{
    char currentChar = text[index];
    char* result = calloc(1, sizeof(char));
    result[0] = '\0';
    int resultSize = 0;
    struct Token token;

    if(currentChar >= '0' && currentChar <= '9') 
    {
        while(currentChar >= '0' && currentChar <= '9') 
        {
            resultSize++;
            result = realloc(result, resultSize + 1);
            result[resultSize] = '\0';
            result[resultSize-1] = currentChar;
            index++;
            currentChar = text[index];
        }
        token.value = atoi(result);
        strcpy(token.type, INTEGER);
        return token;
    }

    if(currentChar == '+' || currentChar == '-') {

    }
    
}

