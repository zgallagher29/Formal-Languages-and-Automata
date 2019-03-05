%{
#include <stdio.h>
#include <stdlib.h>

extern int yylex();
void yyerror(char* msg);
%}


%union {
    float f; 
    int i; 

   
}

%token <f> FLOAT
%token <i> INT
%type <f> E N T F




%% 

S: E            {printf("%.6g\n",$1);}     
 ; 
E: E '+' T      {$$ = $1+$3; }
 | T            {$$ = $1;}
 ;
T: T '*' F      {$$ = $1*$3;}
 | F            {$$ = $1;}
 ;
F: '(' E ')'    {$$ = $2;}     
 | N            {$$ = $1;}
 ;
N: FLOAT        {$$ = $1;}   
 | INT          {$$ = $1;}   
 ;

 
 
%% 

void yyerror(char *msg) {

    fprintf(stderr, "%s\n",msg);
    exit(1);
}

int main(){
    yyparse();
    return 0;
}