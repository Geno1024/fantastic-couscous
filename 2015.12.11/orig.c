#include "stdafx.h"
#include<stdio.h>
#include<string.h>
int main(int argc, char* argv[])
{
int max_word(char str[80]);
 char str[80],str1[20];
 printf("Please input a string!\n");
 gets(str);
 str1[20]=max_word;
 printf("the longest word is %s.\n"str1[20]);
 return 0;
 }
 
int max_word(char str[80])
{
 char i=0,j,d[20],b[20];
 for(s=0;;s++) 
 { 
  for(;;i++)  
 {  
  if(str[i]=='\0') 
 { 
   b[s]=str[i];
   break;  
  }
 str[i]='\0';
  i+=1;
  }
  if(strlen(b[s])>=strlen(b[s-1]))
   d[]=b[s]; 
 }
 return(d);  
}