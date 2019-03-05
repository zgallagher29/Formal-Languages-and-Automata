%{
#include <stdio.h>
#include <stdlib.h>
#include "y.tab.h"


%}

%option noyywrap

%%

[0-9]*\.[0-9]+"f"?              {yylval.f = atof(yytext); return FLOAT;}
[0-9]+                          {yylval.i = atoi(yytext); return INT;}
[+()*]                          {return yytext[0];}                          
[ \t\f\v\n]                     { ; }


%%