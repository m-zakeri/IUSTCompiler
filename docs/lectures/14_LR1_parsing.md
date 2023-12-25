# LR(1) Parsing and LR(1) Grammars


# <center><img src="pictures/compiler.jpg" width="300"/>



LR(1) parsing, also known as canonical LR(1) parsing, is an extension of LR(0) parsing. It uses similar concepts as SLR, but it uses one lookahead symbol instead of none. The idea is to get as much as possible out of one lookahead symbol. The LR(1) item is an LR(0) item combined with lookahead symbols possibly following the production locally within the same item set. For instance, an LR(0) item could be `S → ·S + E`, and an LR(1) item could be `S → ·S + E , +`. Similar to SLR parsing, lookahead only impacts reduce operations in LR(1). If the LR(1) parsing action function has no multiply defined entries, then the given grammar is called an LR(1) grammar.

# LR(1) Closure
Similar to LR(0) closure, but also keeps track of the lookahead symbol. If `I` is a set of items, `CLOSURE(I)` is the set of items such that:

1. Initially, every item in `I` is in `CLOSURE(I)`,
2. If `A → α · B` and `B → γ` is a production whose closures are not in `I` then add the item `B → γ` , `FIRST(β)` to `CLOSURE(I)`.
3. In step (2) if `β → ε` then add the item `B → γ , δ` to `CLOSURE(I)`.
4. For recursive items with form `A → ·Aα , δ ` and ``A → ·β , δ` replace the items with `A → ·Aα , δ, FIRST(α)` and `A → ·β , δ, FIRST(α)`.
Apply these steps (2), (3), and (4) until no more new items can be added to `CLOSURE(I)`.

# LR(1) GOTO and States
Initial state: start with `[S' → S$ , $]` as the kernel of `I0`, then apply the `CLOSURE(I)` operation. The GOTO function is analogous to GOTO in LR(0) parsing.

# LR(1) Items
An LR(1) item is a pair `[α; β]`, where `α` is a production from the grammar with a dot at some position in the RHS and `β` is a lookahead string containing one symbol (terminal or EOF). What about LR(1) items? Several LR(1) items may have the same core. For instance, `[A ::= X · Y Z; a]` and `[A ::= X · Y Z; b]` would be represented as `[A ::= X · Y Z; {a, b}]`.




# LR(1) Parsing and LR(1) Grammars

LR(1) parsing, also known as canonical LR(1) parsing, is an extension of LR(0) parsing. It uses similar concepts as SLR, but it uses one lookahead symbol instead of none. The idea is to get as much as possible out of one lookahead symbol. The LR(1) item is an LR(0) item combined with lookahead symbols possibly following the production locally within the same item set. For instance, an LR(0) item could be `S → ·S + E`, and an LR(1) item could be `S → ·S + E , +`. Similar to SLR parsing, lookahead only impacts reduce operations in LR(1). If the LR(1) parsing action function has no multiply defined entries, then the given grammar is called an LR(1) grammar.

# LR(1) Parsing Table: Example

Let's consider the following grammar:

```
(0) S' → S$
(1) S → CC
(2) C → aC
(3) C → d
```

First, we augment the grammar by adding a new start symbol and a new production that starts with the old start symbol followed by a special end marker `$`. Then we compute the closure of the set of items derived from the new start symbol. We repeat this process for each new state until no more new states can be added. For each state and input symbol, we determine the action to take (shift, reduce, or go to) based on the transitions in the state machine. Finally, we write the resulting actions into the ACTION and GOTO fields of the parsing table.

# LR(1) Parsing Table: Exercise

Let's consider the following grammar:

```
S → E + S | E
E → num
```

We would follow the same steps as in the example to construct the LR(1) parsing table for this grammar. However, since the grammar is quite simple, the resulting table should also be relatively straightforward.

Remember, the goal is to identify any conflicts in the parsing table. A conflict occurs when there are multiple possible actions for a given state and input symbol. If there are no conflicts, then the grammar is suitable for LR(1) parsing.

