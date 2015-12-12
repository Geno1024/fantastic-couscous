#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* getLongestWord(char *sentence, char *longestWord)
{
	char wordBuffer[40];
	int wordBufferPointer = 0;
	int longestWordSize = 0;
	int flag = 0;
	for(int i = 0; i < 80; i++, wordBufferPointer++)
	{
		switch(sentence[i])
		{
			case '\0':
				goto label1;
			case '.':
				goto label1;
			case '\n':
				goto label1;
			case ' ':
				if(wordBufferPointer > longestWordSize)
					strcpy(longestWord, wordBuffer);
					longestWordSize = wordBufferPointer;
				wordBufferPointer = -1;
				break;
			default:
				wordBuffer[wordBufferPointer] = sentence[i];
		}
	}
	label1: 		
		if(wordBufferPointer > longestWordSize)
			strcpy(longestWord, wordBuffer);
		return longestWord;
}

int main()
{
	char sentence[80];
	char longestWord[40];
	printf("Input a sentence.\n");
	fgets(sentence, 80, stdin);
	getLongestWord(sentence, longestWord);
	printf("The longest word is: %s\n", longestWord);
	return 0;
}
