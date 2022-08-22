# re / bruh

This challenge is brainfuck, but the symbols have been replaced with cool Gen-Z slang:

```python
bfmap = {
    "on god": "+",
    "frfr": "-",
    "no cap": "[",
    "cap": "]",
    "deadass": ">",
    "sus": "<",
    "bussin": "."
}
```

So the code translates to:
```brainfuck
++++++++++[>+++++++++>+++++++>++++++++++++>++++++++++>++++++++++<<<<<-]>-----.>-----.+++++++.>+++.>--.<---------.>-.>+++++.+++++.<+++++.<+++.>---.>---.<----.>+++.+.<.++++.--.>+.<--.+++++++.>++.<.>.<-------.+++.>.<<.>++++++.---------.>-----.++.--.<++++++.>+.<<-.+++++++++.
```

Which prints: `UAH{brainfuck_no_cap_frfr_bruh_moment}`