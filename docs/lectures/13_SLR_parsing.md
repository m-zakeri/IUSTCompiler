# Simple LR Parsing (SLR or SLR(1))

<img src="../pictures/compiler.jpg" width="300" class="center"/>


Simple LR parsing, also known as SLR or SLR(1), is an extension of LR(0) parsing. It introduces a single token of lookahead to help resolve conflicts between shift and reduce operations. 

For each reduction item `A → γ·`, the parser looks at the lookahead symbol `c`. It applies the reduction only if `c` is in the `FOLLOW(A)` set, which contains all the terminal symbols that can appear immediately after `A` in a sentential form derived from the start symbol.

# SLR Parsing Table

The SLR parsing table eliminates some conflicts compared to the LR(0) table. It is essentially the same as the LR(0) table, but with reduced rows. Reductions do not fill entire rows. Instead, reductions `A → γ·` are added only in the columns of symbols in `FOLLOW(A)`.

# SLR Grammar

An SLR grammar is a context-free grammar for which the SLR parsing table does not have any conflicts. In other words, an SLR grammar is one that can be parsed by an SLR parser without encountering any shift/reduce or reduce/reduce conflicts.

# SLR Parsing: Example

The SLR parsing algorithm is similar to the LR(0) parsing algorithm, but with the addition of considering the lookahead symbol when deciding whether to shift or reduce. Here is a simplified version of the algorithm:

1. Initialize the stack with the start symbol of the grammar and the special end marker `$`.
2. Read the first input symbol.
3. Look up the current state and input symbol in the ACTION field of the parsing table to get the action to perform.
4. If the action is a shift, push the input symbol onto the stack and move to the next state. If the action is a reduce, replace the top of the stack with the left-hand side of the grammar rule. If the action is a go to, move to the next state without changing the stack.
5. Repeat steps 2-4 until the entire input has been read and the stack contains only the start symbol and the end marker.

# SLR Parsing: Example

Let's consider a simple grammar:

```
E -> E + T | T
T -> F | (E)
F -> id
```

And the example input `id + id`.

We start by initializing the stack with the start symbol `E` and the end marker `$`. Then we read the first input symbol `id`. According to the parsing table, we shift `id` onto the stack and move to state 2. We continue this process until we have consumed all the input symbols.

At the end of the parsing process, if the stack contains only the start symbol and the end marker, the input string is accepted. Otherwise, it is rejected.

# Expanding the Concepts

## SLR Parsing

SLR (Simple LR) parsing is an extension of LR(0) parsing. It introduces a single token of lookahead to help resolve conflicts between shift and reduce operations. For each reduction item `A → γ·`, the parser looks at the lookahead symbol `c`. It applies the reduction only if `c` is in the `FOLLOW(A)` set, which contains all the terminal symbols that can appear immediately after `A` in a sentential form derived from the start symbol.

## SLR Parsing Scope

The scope of an SLR parser refers to the set of languages it can recognize. An SLR parser can recognize a context-free language if and only if the language is unambiguous and does not contain left recursion. However, unlike LR(0) parsers, SLR parsers can handle certain types of ambiguous grammars by considering the lookahead symbol when deciding whether to shift or reduce.

## SLR Parsing Limitations

Despite its advantages, SLR parsing still has limitations. One of the main limitations is that it cannot handle certain types of ambiguous grammars, such as those with left recursion or grammars that require more than one token of lookahead to resolve ambiguities. Additionally, the SLR parsing algorithm requires additional computational resources compared to LR(0) parsing due to the need to calculate the `FOLLOW(A)` set for each non-terminal.

## Show That the Following Grammar Is Not SLR

Let's consider the following grammar:

```
(0) S' → S$
(1) S → AaAb
(2) S → BbBa
(3) A → ε
(4) B → ε
```

If we try to construct the SLR parsing table for this grammar, we will encounter two reduce-reduce conflicts in the action cells for `state 0, a` and `state 0, b`. This is because both `A → ε` and `B → ε` are applicable in these cases, and neither can be decided upon solely based on the lookahead symbol. Therefore, this grammar is not SLR.

In general, to show that a grammar is not SLR, we need to construct the SLR parsing table and check for any reduce-reduce conflicts. If we find any such conflicts, then the grammar is not SLR.

# SLR Parsing: Example

Let's consider a simple grammar:

```
E -> E + T | T
T -> F | (E)
F -> id
```

And the example input `id + id`.

We start by initializing the stack with the start symbol `E` and the end marker `$`. Then we read the first input symbol `id`. According to the parsing table, we shift `id` onto the stack and move to state 2. We continue this process until we have consumed all the input symbols.

At the end of the parsing process, if the stack contains only the start symbol and the end marker, the input string is accepted. Otherwise, it is rejected.
