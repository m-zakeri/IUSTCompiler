# Mastering LR Parsing Errors

<img src="../pictures/compiler.jpg" width="300" class="center"/>


LR parsing is a powerful technique used in computer programming language compilers and other associated tools. One of the challenges it faces is handling errors. An LR parser will detect an error when it consults the parsing action table and finds an error entry. Errors are never detected by consulting the goto table. 

## Panic-Mode Error Recovery

In LR parsing, we can implement panic-mode error recovery as follows:

1. Scan down the stack until a state `s` with a goto on a particular nonterminal `A` is found.
2. Zero or more input symbols are then discarded until a symbol `a` is found that can legitimately follow `A`.
3. The parser then stacks the state `GOTO(s, A)` and resumes normal parsing.

This approach allows the parser to recover from errors by discarding erroneous input and resuming normal parsing.

## Phrase-Level Error Recovery

Phrase-level recovery is another strategy for handling errors in LR parsing. This approach involves examining each error entry in the LR parsing table and deciding, based on language usage, the most likely programmer error that would give rise to that error. An appropriate recovery procedure can then be constructed, presumably modifying the top of the stack and/or first input symbols in a way deemed appropriate for each error entry.

In designing specific error-handling routines for an LR parser, we can fill in each blank entry in the action field with a pointer to an error routine that will take the appropriate action selected by the compiler designer. The actions may include insertion or deletion of symbols from the stack or the input or both, or alteration and transposition of input symbols. We must make our choices so that the LR parser will not get into an infinite loop.

## Example of Error Recovery Using LR Parser

Consider the following grammar:

```
E → E + E 
E → E * E 
E → ( E ) 
E → id
```

Suppose we want to parse the input string `id+)$`. Here's how the LR parser would work:

```
STACK INPUT
0    id+)$
0id3 +)$
0E1  +)$
0E1 + 4)$
0E1 + 4id3
0E1 + 4E7
0E1
$
```

In this example, the LR parser successfully parses the input string `id+)$` according to the given grammar. Note that the actual parsing process would involve more steps and more complex entries in the parsing table.

Understanding and mastering these error recovery strategies can significantly improve the robustness and reliability of LR parsers.


# LR Parsing Error Recovery: A Comprehensive Guide

Error recovery is a crucial aspect of LR parsing, which is widely used in computer programming language compilers and other associated tools. An LR parser will detect an error when it consults the parsing action table and finds an error entry. Errors are never detected by consulting the goto table. 

## Implementing Panic-Mode Error Recovery

In LR parsing, we can implement panic-mode error recovery as follows:

1. Scan down the stack until a state `s` with a goto on a particular nonterminal `A` is found.
2. Zero or more input symbols are then discarded until a symbol `a` is found that can legitimately follow `A`.
3. The parser then stacks the state `GOTO(s, A)` and resumes normal parsing.

This approach allows the parser to recover from errors by discarding erroneous input and resuming normal parsing.

## Phrase-Level Error Recovery

Phrase-level recovery is another strategy for handling errors in LR parsing. This approach involves examining each error entry in the LR parsing table and deciding, based on language usage, the most likely programmer error that would give rise to that error. An appropriate recovery procedure can then be constructed, presumably modifying the top of the stack and/or first input symbols in a way deemed appropriate for each error entry.

In designing specific error-handling routines for an LR parser, we can fill in each blank entry in the action field with a pointer to an error routine that will take the appropriate action selected by the compiler designer. The actions may include insertion or deletion of symbols from the stack or the input or both, or alteration and transposition of input symbols. We must make our choices so that the LR parser will not get into an infinite loop.

## LR Parsing Error Recovery: Example

Consider the following expression grammar:

```
E → E + E | E * E | (E) | id
```

Let's say we want to parse the input string `id+)$`. Here's how the LR parser would work:

```
STACK INPUT
0   id+)$
0id3 +)$
0E1 +)$
0E1 + 4)$
0E1 + 4id3
0E1 + 4E7
0E1
$
```

In this example, the LR parser successfully parses the input string `id+)$` according to the given grammar. Note that the actual parsing process would involve more steps and more complex entries in the parsing table.

## Error Routines for LR Parsing

Let's consider an LR parsing table with error routines for the expression grammar. Suppose we have four errors:

- **e1**: Push state 3 (the goto of states 0, 2, 4 and 5 on id); issue diagnostic "missing operand."
- **e2**: Remove the right parenthesis from the input; issue diagnostic "unbalanced right parenthesis."
- **e3**: Push state 4 (corresponding to symbol +) onto the stack; issue diagnostic "missing operator."
- **e4**: Push state 9 (for a right parenthesis) onto the stack; issue diagnostic "missing right parenthesis."

These error routines demonstrate how LR parsers can recover from common syntax errors encountered during parsing.