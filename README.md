# Formal Languages and Automata
Class work for graduate class Formal Languages and Automata

## Homework 6

### Prompt
Read about GNU Bison (https://www.gnu.org/software/bison/) and use it to generate a parser for our arithmetic
expression grammar:  
  𝐺 = ({𝐸, 𝑇, 𝐹},{𝑎, 𝑏, 𝑐, (, )},𝑅, 𝐸) with the rule set R given by:  
  𝐸 → 𝐸 + 𝑇 | 𝑇  
  𝑇 → 𝑇 ∗ 𝐹 | 𝐹  
  𝐹 → (𝐸) | 𝑛  
  𝑛 → 𝑖𝑛𝑡𝑒𝑔𝑒𝑟 | 𝑓𝑙𝑜𝑎𝑡  

Demonstrate the execution of your parser on various arithmetic expressions, evaluating them to numeric
values. Turn in a demonstration of bison and the parser your generate.

### How to Run 

From HW6 Directory:
You will probably able to just skip to step 4, but if that doesn't work then do all the steps. 

1. yacc -d syntax.y
2. lex semantics.l
3. cc lex.yy.c y.tab.c -o parser
4. ./parser
5. enter your desired expression
6. Press enter then Press CTRL D
  
### Limitations
- All numbers must be floats or all numbers must be integers
- Only one expression per run

### Example Run

![alt text](https://github.com/zgallagher29/Formal-Languages-and-Automata/issues/1#issue-417143433)
