# Expanding the Concepts

# <center><img src="pictures/compiler.jpg" width="300"/>


## Representing Item Sets

In the context of LR(0) parsing, an item set represents the current state of the parser. Each item in the set corresponds to a production in the grammar, with a dot indicating the current position in the production. For example, if we have a production `A -> BC`, there will be four items corresponding to this production:

* `A -> .BC`
* `A -> B.C`
* `A -> BC.`
* `A -> B.C.`

These items represent the different stages of recognizing the production `A -> BC`.

## Closure and Goto of Item Sets

The closure operation takes a set of items and produces a new set containing all items that can be derived from the original set. This is done through a series of steps:

1. Add every item in the original set to the closure set.
2. For each item in the closure set that is of the form `A -> α.Bβ`, check if there is a production `B -> γ` in the grammar. If so, add the item `B -> .γβ` to the closure set.
3. Repeat step 2 until no more new items can be added to the closure set.

The GOTO operation, on the other hand, is used to determine the next state based on the current state and the next input symbol. It is defined as the closure of the set of all items of the form `A -> αB.β`, where `A -> α.Bβ` is in the current state.

## Closure and Goto of Item Sets: Example

Let's consider a simple grammar:

```
E -> E + T | T
T -> F | (E)
F -> id
```

We start with the initial state `I0 = {E -> .E + T}`. We apply the closure operation to get the closure of `I0`:

```
I0 = {E -> .E + T, E -> E + .T}
```

Then, we apply the GOTO operation with the input symbol `E` to get the next state:

```
GOTO(I0, E) = {E -> E + .T, E -> .T}
```

We continue this process until we reach the final state, which indicates that the input string is valid according to the grammar.

## Canonical Collection of Sets of LR(0) Items

To construct the parsing table, we need to compute the canonical collection of sets of LR(0) items for an augmented grammar. This involves creating a set of states, where each state represents a set of items. The transitions between states are determined by the GOTO operations.

## LR(0) Item Sets: Example

Let's consider a slightly more complex grammar:

```
S -> CC
C -> aC | d
```

We start by augmenting the grammar to handle left recursion:

```
S' -> SC'
C' -> aC' | d
```

We then compute the item set for the augmented grammar:

```
I0 = {S' -> .SC', C' -> .aC' | d}
```

We continue this process until we reach the final state.

## Structure of the LR Parsing Table

The LR parsing table consists of two parts: a parsing-action function `ACTION` and a goto function `GOTO`. The `ACTION` function determines what action the parser should take based on the current state and the next input symbol. The `GOTO` function determines the next state based on the current state and the next input symbol.

# LR(0) Parsing: Example

Consider the following parsing table generated from the grammar `E -> E + T | T` :

```
ACTION GOTO
State int+;()ET
0     s9    s8,13
1     Accept
2     Reduce E -> T + E
3     s5,s4
4     Reduce E -> T;
5     s9,s8,23
6     Reduce T -> (E)
7     s6
8     s9,s8,73
9     Reduce T -> int
```

This table shows that if the parser is in state 0 and reads an integer, it shifts the integer and moves to state 9. If it reads a plus sign, it reduces `E -> T` and stays in state 1. If it reads a left parenthesis, it reduces `T -> (E)` and moves to state 6. And so on.

# LR(0) DFA Construction: Example

Let's consider a slightly more complex grammar:

```
S -> E
E -> T;
E -> T + E
T -> int
T -> (E)
```

We start by adding the initial item `S -> .E` to the initial state:

```
State 0:
S -> .E
```

We then




# Structure of the LR Parsing Table: Example

Let's consider the grammar `G'` from the previous example:

(0) `S'` → `S$`
(1) `S → CC`
(2) `C → aC`
(3) `C → d`

The parsing table for this grammar would be constructed based on the item sets and the GOTO and ACTION functions. The exact contents of the table would depend on the specific implementation of the LR parser, but it might look something like this:

| State | Input | Action | Next State |
|-------|-------|--------|------------|
| 0    | S'   | Shift | 1         |
| 1    | C    | Shift | 2         |
| 2    | a    | Shift | 2         |
| 2    | d    | Reduce |          |
| ...  | ...  | ...   | ...       |

The 'Action' column indicates whether the parser should shift (read the next input symbol and push it onto the stack), reduce (apply a grammar rule to the top of the stack), or go to (move to a new state without consuming any input symbols).

# LR-parsing algorithm i

The LR-parsing algorithm works as follows:

1. Initialize the stack with the start symbol of the grammar and the special end marker `$`.
2. Read the first input symbol.
3. Look up the current state and input symbol in the ACTION field of the parsing table to get the action to perform.
4. Perform the action: if it's a shift, push the input symbol onto the stack and move to the next state. If it's a reduce, replace the top of the stack with the left-hand side of the grammar rule. If it's a go to, move to the next state without changing the stack.
5. Repeat steps 2-4 until the entire input has been read and the stack contains only the start symbol and the end marker.

# LR-parsing algorithm ii

The second LR-parsing algorithm is similar to the first one, but instead of using the ACTION field of the parsing table, it uses the GOTO field to determine the next state. This allows the parser to avoid reading the next input symbol until it knows whether it needs to shift or go to.

# LR(0) parsing table: Example

The LR(0) parsing table provides the same functionality as the LR parsing algorithms described above, but in a more compact form. It consists of two parts: the ACTION table and the GOTO table.

The ACTION table maps each state and input symbol to an action (shift, reduce, accept, or error). The GOTO table maps each state and grammar symbol to a next state.

Here is an example of an LR(0) parsing table for a simple grammar:

| State | Input | Action | Next State |
|-------|-------|--------|------------|
| 0    | a    | Shift | 1         |
| 1    | b    | Reduce |           |
| 0    | b    | Error |           |

This table tells us that if we are in state 0 and read an 'a', we should shift it onto the stack and move to state 1. If we are in state 1 and read a 'b', we should reduce by the rule `A -> aB`. If we are in state 0 and read a 'b', we should report an error.

# LR(0) Parsing: Example

Let's consider the following parsing table for the grammar `G`:

(0) `S'` → `S$`
(1) `S → CC`
(2) `C → aC`
(3) `C → d`

And the example input `add$`.

We start by initializing the stack with the start symbol `S'` and the end marker `$`. Then we read the first input symbol 'a'. According to the parsing table, we shift 'a' onto the stack and move to state 1. We continue this process until we have consumed all the input symbols.

At the end of the parsing process, if the stack contains only the start symbol and the end marker, the input string is accepted. Otherwise, it is rejected.

# All LR parsers (LR(0), LR(1), LALR(1), and SLR(1)) behave in this fashion

All LR parsers follow a similar process: they initialize the stack with the start symbol and the end marker, then read the input symbols one by one, looking up actions in the parsing table to decide whether to shift, reduce, or go to. The only difference between them lies in the construction of the parsing table, which depends on the specific variant of LR parsing being used.

# LR(0) Parsing

LR(0) parsing is a type of bottom-up parsing method used in compiler design. It uses a finite automaton to guide the parsing process. The LR(0) parser reads the input symbols from left to right (L), applies the productions in reverse order (R), and looks ahead zero symbols (0) to decide what action to take.

The LR(0) parser uses two tables during the parsing process: the ACTION table and the GOTO table. The ACTION table maps each state and input symbol to an action (shift, reduce, accept, or error). The GOTO table maps each state and grammar symbol to a next state.

# LR(0) Parser Scope

The scope of an LR(0) parser refers to the set of languages it can recognize. An LR(0) parser can recognize a context-free language if and only if the language is unambiguous and does not contain left recursion.

# LR(0) Limitations

One limitation of LR(0) parsing is that it cannot handle certain types of ambiguous grammars, such as those with left recursion or grammars that require more than one token of lookahead to resolve ambiguities.

# LR(0) Parsing Table with Conflicts

Conflicts in the LR(0) parsing table occur when there are multiple possible actions for a given state and input symbol. These conflicts must be resolved before the parsing table can be used effectively. One common way to resolve conflicts is by using operator precedence and associativity rules, or by transforming the grammar to remove the ambiguity.

# LR(0) Grammar: Exercises

To construct the LR(0) parsing table for a given grammar, you would typically follow these steps:

1. Augment the grammar by adding a new start symbol and a new production that starts with the old start symbol followed by a special end marker `$`.
2. Compute the closure of the set of items derived from the new start symbol.
3. Repeat step 2 for each new state until no more new states can be added.
4. For each state and input symbol, determine the action to take (shift, reduce, or go to) based on the transitions in the state machine.
5. Write the resulting actions into the ACTION and GOTO fields of the parsing table.

The exercise asks you to construct the LR(0) parsing table for several different grammars. You would need to follow the steps above for each grammar.

# Which one is LR(0)?

To determine whether a grammar is suitable for LR(0) parsing, you would need to check whether the grammar is unambiguous and does not contain left recursion. If both conditions are met, then the grammar is suitable for LR(0) parsing.

From the given grammars, the ones that are suitable for LR(0) parsing are:

- `S → AB`
- `S → Ab`
- `A → ε`
- `B → b`
- `S → A`
- `S → aa`
- `A → a`

The remaining grammars either contain left recursion (`S → AA` and `A → aA`) or are ambiguous (`S → A`), making them unsuitable for LR(0) parsing.

