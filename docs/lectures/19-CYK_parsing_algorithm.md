# Designing More Powerful Parsers


# <center><img src="pictures/compiler.jpg" width="300"/>



Designing more powerful parsers often involves considering different parsing methods. Two of the most prevalent types of parsers are LL and LR parsers. These parsers are deterministic, directional, and operate in linear time, making them capable of recognizing restricted forms of context-free grammars.

However, parsing more grammars non-directionally poses a challenge, especially when we consider allowing more time-consuming algorithms. To address this, we can employ various strategies:

* **Brute Forcing:** This approach involves enumerating everything possible. While straightforward, it can be computationally expensive due to its exhaustive nature.
* **Backtracking:** This strategy involves trying different subtrees and discarding partial solutions if they prove unsuccessful. This allows the parser to explore different branches of the parse tree until a valid parse is found.
* **Dynamic Programming:** This method involves saving partial solutions in a table for later use. This technique is efficient as it avoids recomputation by storing the result of a subproblem and reusing it when needed. However, dynamic programming requires a non-directional parsing method, which is not inherent in LL and LR parsers.

# Directionality of Parsing Methods

Parsing methods can be categorized into two types: directional and non-directional methods.

Directional methods process the input symbol by symbol from left to right. LL and LR parsers fall under this category. The advantage of directional methods is that parsing starts and makes progress before the last symbol of the input is seen.

Non-directional methods, on the other hand, allow access to input in an arbitrary order. They require the entire input to be in memory before parsing can start. This flexibility allows non-directional parsers to handle more flexible grammars than directional parsers. An example of a non-directional parser is the CYK parser.

# CYK (Cocke-Younger-Kasami)

The CYK algorithm is one of the earliest recognition and parsing algorithms, developed independently by three Russian scientists: J. Cocke, D.H. Younger, and T. Kasami. This algorithm uses a bottom-up parsing approach, reducing already recognized right-hand sides of a production rule to its left-hand side non-terminal. As it is non-directional, it accesses input in an arbitrary order, necessitating the entire input to be in memory before parsing can begin.

# CYK Parsing

# <center><img src="pictures/compiler.jpg" width="300"/>
 

The CYK algorithm operates on a dynamic programming or table-filling approach. It constructs solutions compositionally from sub-solutions. Notably, the CYK algorithm recognizes any context-free grammar in Chomsky Normal Form. It operates on a binary parse tree.

# Chomsky Normal Form

A Context-Free Grammar (CFG) is said to be in Chomsky Normal Form (CNF) if each rule is of the form `A → BC` or `A → a`, where `a` is any terminal, and `A`, `B`, `C` are non-terminals. `B` and `C` cannot be the start variable. We allow the rule `S → ε` if `ε` is in `L`.

# CYK Algorithm: Basic Idea

The CYK algorithm works as follows:

1. For a grammar `G` (in CNF) and a word (or string) `w`:
   * For every substring `v1` of length 1, find all non-terminals `A` such that `Av1 ⇒ *`.
   * For every substring `v2` of length 2, find all non-terminals `A` such that `Av2 ⇒ *`.
   * ...
   * For the unique substring `w` of length `|w|`, find all non-terminals `A` such that `Aw ⇒ *`.
2. Check whether the start symbol `S` belongs to the last set.

For more details about converting a CFG grammar to the CNF form, please refer to the appendix slides.


## Solution Representation for Substring Recognition
In the context of the CYK (Cocke-Younger-Kasami) algorithm, solution representation for substring recognition is essential. The CYK algorithm is a dynamic programming algorithm that is used for parsing context-free grammars. It constructs parse trees by recognizing and combining smaller parse trees. Therefore, the ability to recognize specific subsequences within a larger string is crucial.

## Substring Recognition
Substring recognition is a key component of the CYK algorithm. It involves identifying and recognizing specific subsequences within a larger string. This process is fundamental to the operation of the CYK algorithm, which constructs parse trees by recognizing and combining smaller parse trees. The recognition of these smaller parse trees is done through the recognition table.

## Recognition Table
The recognition table is a two-dimensional array that is used to store the potential non-terminal symbols that can generate a particular substring of the input string. Each cell in the table represents a substring of the input string. The value of a cell indicates the set of non-terminal symbols that can generate the corresponding substring. This table is filled iteratively, with each cell being updated based on the values of its neighboring cells.

## CYK Algorithm: Example Trace
An example trace of the CYK algorithm involves stepping through the algorithm and observing how it processes a given input string and applies the grammar rules. This involves iterating over the input string and the grammar rules, applying the rules, and updating the recognition table accordingly.

## CYK Pseudocode
The CYK algorithm can be represented in pseudocode, which is a high-level description of the algorithm that can be easily understood and translated into any programming language. The pseudocode for the CYK algorithm would involve loops to iterate over the input string and the grammar rules, conditional statements to apply the rules, and data structures like arrays or matrices to store the recognition table.

## CYK Complexity Analysis
The time and space complexity of the CYK algorithm can be analyzed to understand its efficiency. The space complexity of the CYK algorithm is O(n²), where n is the size of the input word. This is because the algorithm uses a n x n table to store the recognition table.

The time complexity of the CYK algorithm is O(|G|n³), where |G| is the size of the grammar and n is the size of the input word. This is because the algorithm needs to iterate over the input string and the grammar rules, which results in a cubic time complexity.

## CYK Parsing: Problems
While the CYK algorithm is powerful, it does come with certain challenges. The high time and space complexity can make it less suitable for large inputs or complex grammars. Additionally, converting the grammar to Chomsky Normal Form (CNF) can sometimes make it difficult to retain the intended structure of the grammar.

## CYK Parsing: Exercises
There are several exercises associated with the CYK algorithm. These exercises provide practical applications of the algorithm and help to deepen understanding of its workings.

For instance, one exercise asks to show the CYK algorithm with a given grammar and input word. Another exercise asks to use the CYK method to determine if a specific string is in the language generated by a given grammar. There are also exercises on modifying the CYK algorithm to count the number of parse trees for a given input string and discussing the probabilistic version of the CYK method.


# CYK Complexity Analysis

The time and space complexity of the CYK algorithm can be analyzed to understand its efficiency. 

The space complexity of the CYK algorithm is O(n²), where n is the size of the input word. This is because the algorithm uses a n x n table to store the recognition table.

The time complexity of the CYK algorithm is O(|G|n³), where |G| is the size of the grammar and n is the size of the input word. This is because the algorithm needs to iterate over the input string and the grammar rules, which results in a cubic time complexity.

The complexity of the grammar |G| is defined as the sum of the lengths of the right-hand sides of all production rules in the grammar.

# CYK Algorithm Pseudocode

The CYK algorithm can be represented in pseudocode, which is a high-level description of the algorithm that can be easily understood and translated into any programming language. The pseudocode for the CYK algorithm would involve loops to iterate over the input string and the grammar rules, conditional statements to apply the rules, and data structures like arrays or matrices to store the recognition table.

The pseudocode for the CYK algorithm is as follows:

```
For i = 1 to n:
 For each variable A:
    We check if A -> b is a rule and b = w[i]
    If so, we place A in cell (i, i) of our table.

For l = 2 to n:
 For i = 1 to n-l+1:
      j = i+l-1
       For k = i to j-1:
          For each rule A -> BC: 
       We check if (i, k) cell contains B and (k + 1, j) cell contains C:
            If so, we put A in cell (i, j) of our table.

We check if S is in (1, n):
 If so, we accept the string
 Else, we reject.
```

# CYK Parsing: Exercise Solutions

1. For the given grammar and input word, the CYK algorithm can be shown by manually applying the algorithm's steps to the given input and grammar.
2. To determine if the string `w = aaabbbb` is in the language generated by the grammar `S → aSb | b`, we can apply the CYK algorithm to this string and grammar.
3. To modify the CYK algorithm to count the number of parse trees of a given input string, we can add a counter to the algorithm that increments whenever a new parse tree is formed.
4. For the probabilistic version of the CYK method (P-CYK), weights (probabilities) are stored in the table instead of booleans, so P[i,j,A] will contain the minimum weight (maximum probability) that the substring from i to j can be derived from A. Further extensions of the algorithm allow all parses of a string to be enumerated from lowest to highest weight (highest to lowest probability).



# CYK Complexity Analysis

The time and space complexity of the CYK algorithm can be analyzed as follows:

The space complexity of the CYK algorithm is O(n²), where n is the size of the input word. This is because the algorithm uses a n x n table to store the recognition table.

The time complexity of the CYK algorithm is O(|G|n³), where |G| is the size of the grammar and n is the size of the input word. This is because the algorithm needs to iterate over the input string and the grammar rules, which results in a cubic time complexity.

The complexity of the grammar |G| is defined as the sum of the lengths of the right-hand sides of all production rules in the grammar, denoted as:

|G| = ∑_{(A→v)∈P} (1 + |v|)

# CYK Algorithm Pseudocode

The CYK algorithm can be represented in pseudocode, which is a high-level description of the algorithm that can be easily understood and translated into any programming language. The pseudocode for the CYK algorithm would involve loops to iterate over the input string and the grammar rules, conditional statements to apply the rules, and data structures like arrays or matrices to store the recognition table.

The pseudocode for the CYK algorithm is as follows:

```
For i = 1 to n:
 For each variable A:
   We check if A -> b is a rule and b = w[i]
   If so, we place A in cell (i, i) of our table.

For l = 2 to n:
 For i = 1 to n-l+1:
     j = i+l-1
      For k = i to j-1:
         For each rule A -> BC: 
      We check if (i, k) cell contains B and (k + 1, j) cell contains C:
           If so, we put A in cell (i, j) of our table.

We check if S is in (1, n):
 If so, we accept the string
 Else, we reject.
```

# CYK Parsing: Exercise Solutions

1. For the given grammar and input word, the CYK algorithm can be shown by manually applying the algorithm's steps to the given input and grammar.
2. To determine if the string `w = aaabbbb` is in the language generated by the grammar `S → aSb | b`, we can apply the CYK algorithm to this string and grammar.
3. To modify the CYK algorithm to count the number of parse trees of a given input string, we can add a counter to the algorithm that increments whenever a new parse tree is formed.
4. For the probabilistic version of the CYK method (P-CYK), weights (probabilities) are stored in the table instead of booleans, so P[i,j,A] will contain the minimum weight (maximum probability) that the substring from i to j can be derived from A. Further extensions of the algorithm allow all parses of a string to be enumerated from lowest to highest weight (highest to lowest probability).