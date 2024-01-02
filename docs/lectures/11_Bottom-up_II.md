
## Bottom-Up Parsing Process

<img src="../pictures/compiler.jpg" width="300" class="center"/>

Bottom-up parsing is the process of reducing an input string to the start symbol S of the grammar. At each reduction step, a specific substring matching the body of a production (RHS) is replaced by the nonterminal at the head of that production (LHS). The key decisions during bottom-up parsing are about when to reduce and about what production to apply, as the parse proceeds.

## Handle Pruning

Bottom-up parsing during a left-to-right scan of the input constructs a right-most derivation in reverse. A "handle" is a substring that matches the body of a production, and whose reduction represents one step along the reverse of a rightmost derivation.

## Shift-Reduce Parsing

Shift-reduce parsing is a form of bottom-up parsing in which a stack holds grammar symbols and an input buffer holds the rest of the string to be parsed. Primary operations are shift and reduce. During a left-to-right scan of the input string, the parser shifts zero or more input symbols onto the stack, until it is ready to reduce a string of grammar symbols on top of the stack. It then reduces to the head of the appropriate production with number Rx. The parser repeats this cycle until it has detected an error or until the stack contains the start symbol and the input is empty.

### Shift-Reduce Parsing Notations

We use $ to mark the bottom of the stack and also the right end of the input. Split string into two substrings, right and left, the dividing point is marked by a |. Right substring is still not examined by parser (a string of terminals). Left substring has both terminals and non-terminals.

### Shift-Reduce Parsing Example

Let's consider the following productions:
```
r1  S->E 
r4  E->T
r2 E ->E+T 
r3  T->(E)
r5  T ->num
```
And the input string `|num+(num+num)$`. The parsing process would go as follows:


```
|num+(num+num)     shift
num|+(num+num)   reduce(r5)   
T|+(num+num)    reduce(r4)
E|+(num+num)  shift
E+|(num+num)   shift
E+(|num+num)   shift
E+(num|+num)  reduce(r5)
E+(T|+num)   reduce(r4)
E+(E|+num)   shift
E+(E+|num)   shift
E+((E+num|)   reduce(r5)
E+(E+T|)    reduce(r2)
E+(E|)   shift
E+(E)    reduce(r3)
E+T    reduce(r2)
E|    reduce(r1)
S|



```
Here, `shift` means pushing the next input symbol onto the top of the stack, and `reduce` means popping zero or more symbols off the stack (production RHS) and pushing a non-terminal on the stack (production LHS)


### Shift-Reduce Parsing Stack

Left substring can be implemented by a stack. Top of the stack is the | symbol. Shift pushes a terminal on the stack. Reduce pops Zero or more symbols of the stack (production RHS) and pushes a non-terminal on the stack (production LHS).

## Conflicts During Shift-Reduce Parsing

There are context-free grammars for which shift-reduce parsing cannot be used. Every shift-reduce parser for such a grammar can reach a configuration in which the parser, knowing the entire stack and also the next k input symbols, cannot decide:

1. Whether to shift or to reduce (a shift/reduce conflict)
2. Or cannot decide which of several reductions to make (a reduce/reduce conflict)


## Final Thoughts

Remember, mastering these concepts takes time and practice. Don't hesitate to ask questions or seek clarification if something is unclear. Happy studying!



# Compiler Design Lesson: Bottom-Up Parsing Process and LR Parsing

## Introduction

Bottom-up parsing is a fundamental concept in compiler design. It involves reducing an input string to the start symbol S of the grammar. At each reduction step, a specific substring matching the body of a production (RHS) is replaced by the nonterminal at the head of that production (LHS). The key decisions during bottom-up parsing are about when to reduce and about what production to apply, as the parse proceeds.

## LR Parsing and LR Grammars

LR parsing is the most prevalent type of bottom-up parser today. The term "LR" stands for left-to-right scanning of the input and constructing a rightmost derivation in reverse. The "k" in LR(k) refers to the number of input symbols of lookahead that are used in making parsing decisions. The cases where k = 0 or k = 1 are of practical interest. When (k) is omitted, k is assumed to be 1. LR parsers are table-driven, similar to nonrecursive LL parsers.

## LR(k) Parsers and Grammars

A grammar for which we can construct a parsing table using an LR parsing algorithm is said to be an LR grammar. The class of grammars that can be parsed using LR methods is a proper superset of the class of grammars that can be parsed with predictive or LL methods. For a grammar to be LL(k), we must be able to recognize the use of a production by seeing only the first k symbols of what its right side derives.

For a grammar to be LR(k), we must be able to recognize the occurrence of the right side of a production in a right-sentential form, with k input symbols of lookahead. This requirement is far less stringent than the one for LL(k) grammars. The principal drawback of the LR method is that it is too much work to construct an LR parser by hand for a typical programming-language grammar. A specialized tool, an LR parser generator, is needed.

## Variants of LR Parsers

There are several variants of LR parsers: SLR parsers, LALR parsers, canonical LR(1) parsers, minimal LR(1) parsers, and generalized LR parsers (GLR parsers). LR parsers can be generated by a parser generator from a formal grammar defining the syntax of the language to be parsed. They are widely used for the processing of computer languages. An LR parser reads input text from left to right without backing up and produces a rightmost derivation in reverse. The name "LR" is often followed by a numeric qualifier, as in "LR(1)" or sometimes "LR(k)". To avoid backtracking or guessing, the LR parser is allowed to peek ahead at k lookahead input symbols before deciding how to parse earlier symbols. Typically k is 1 and is not mentioned.

## Conclusion

Mastering these concepts takes time and practice. Understanding the difference between LL and LR parsing, and the various types of LR parsers, is crucial for effective compiler design. Don't hesitate to ask questions or seek clarification if something is unclear. Happy studying!