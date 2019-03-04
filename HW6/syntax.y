%{
#include <stdio.h>
#include <stdlib.h>

extern int yylext();
%}


%union {
    float f; 
    int i; 
}

%token <f> FLOAT
%token <i> INTEGER
%type <f> E T F

%% 

S: E
 ; 
E: E '+' T      {$$ = $1 + $3; }
 | T            {$$ = $1;}
 ;
T: T '*' F      {$$ = $1 * $3;}
 | F            {$$ = $1;}
 ;
F: '(' E ')'    {$$ = $2;}     
 | FLOAT        {$$ = $1;}
 | INTEGER      {$$ = $1;}
 ; 
%% 

void yyerror(char *msg) {

    fprint(stderr, "%s\n",msg);
    exit(1);
}