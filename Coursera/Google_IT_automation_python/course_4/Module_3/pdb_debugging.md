Python debugging with pdb
=========================

What is pdb?
------------

Imagine you're developing a Python application designed to analyze vast amounts of textual data to extract sentiment scores. As the application processes data, it occasionally encounters unexpected data formats, causing it to crash. Given the volume of data and the complexity of the application, identifying the root cause of these crashes using simple `print()` statements is becoming increasingly challenging. This is where Python's built-in interactive debugger, `pdb`, comes into play.

The acronym `pdb` stands for "Python DeBugger." It's an interactive debugger for Python programs, allowing you to:

* Set breakpoints

* Step through code

* Inspect variables

* Evaluate arbitrary Python expressions interactively

With `pdb`, you can pause your program at any point, inspect the values of variables, and even change those values if needed.

Using `pdb`
---------

Stepping through code is a fundamental debugging technique that empowers developers to follow the execution flow in detail. By observing code execution step-by-step, you can pinpoint the exact location where a bug or unexpected behavior occurs. Plus, you can get a deeper understanding of how different parts of the codebase interact. This is particularly useful for bugs that don't produce immediate or obvious errors.

To start debugging with pdb, you'll first need to set a breakpoint.

### Step 1: Set a breakpoint

Set a breakpoint where you suspect the issue might be. A breakpoint is simply a spot in the code that tells pdb to pause your code at that specific line. You set breakpoints with pdb.set\_trace(). When you run the code below, the debugger will pause at the line where pdb.set\_trace() is called. You will see a prompt like this:

![Image of a pbd prompt to enter pbd commands. It says pbd() with an editable textbox after it.](image.png)

Copy and paste the code below into a Colab and Jupyter Notebook to see how it works and test some of the pbd commands.

```python
import pdb

def add\_numbers(a, b):

    pdb.set\_trace()  # This will set a breakpoint in the code

    result = a + b

    return result

print(add\_numbers(3, 4))
```

When you run this code, the execution will pause at the `pdb.set\_trace()` line, and you'll be dropped into an interactive debugger session.

### Step 2: Enter the interactive debugger

When the breakpoint is hit, you'll enter the interactive debugger. The debugger will display something like this:
```console

><filename.py.(6)add\_numbers()

->result=a+b

(Pdb)
```

At this point, you can query the variables and see their values. If you try to print the value for the result (p), nothing will be found. Stepping forward using n and running p a second time will show the update to the program.

`n` (next) is just one of the commands you can use to navigate the debugger. Other commands include:

* `a` (args): Show the arguments of the current function.

* b`:` Manually set a persistent breakpoint while in debugger.

* `n` (next): Execute the next line within the current function.

* `s` (step): Execute the current line and stop at the first possible occasion (e.g., in a function that is called).

* `c` (continue): Resume normal execution until the next breakpoint.

* `p` (print): Evaluate and print the expression, e.g., p variable\_name will print the value of variable\_name.

* `Pp` (pretty-print): Pretty-print the value of the expression.

* `q` (quit): Exit the debugger and terminate the program.

* `r` (return): Continue execution until the current function returns.

* `tbreak`: Manually set a temporary breakpoint that goes away once hit the first time.

* `!`: Prefix to execute an arbitrary Python command in the current environment, e.g., `!variable\_name` = "`new\_value`" will set variable\_name to "`new\_value`".

For a full list of commands, please refer to [pdb — The Python Debugger](https://docs.python.org/3/library/pdb.html).

### Step 3: Inspect variables

To inspect the variables, simply type the single character, `p`, then the variable name to see its current value. For instance, if you have a variable in your code named `sentiment\_score`, just type p `sentiment\_score` at the `pdb` prompt to inspect its value.

### Step 4: Modify variables

A big advantage of `pdb` is that you can change the value of a variable directly in the debugger. For example, to change `sentiment\_score` to 0.9, you'd type `!sentiment\_score = 0.9`.

To confirm these changes, use a or directly probe the value with p `<value name>`.

### Step 5: Exit the debugger

When you’re done, simply enter `q` (quit) to exit the debugger and terminate the program.

Post-mortem debugging
---------------------

If your program crashes, you can use pdb to inspect its state at the time of the crash. Run your script with:

```console
python -m pdb your\_script.py
```

If an exception occurs, `pdb` will automatically start and allow you to inspect the problem.

In ordinary circumstances, when running this on a script that works, it just starts at the beginning of the program rather than any breakpoints that you may have originally set. Otherwise, it runs with the same commands (`n, a, p <variable>`, etc.).

Key takeaways
-------------

* `pdb` is Python's built-in interactive debugger for diagnosing and resolving issues in Python applications.

* With `pdb`, you can set breakpoints, step through your code, inspect and modify variables, and evaluate Python expressions interactively.

* `pdb` allows for a more in-depth understanding of code execution flow and aids in identifying the root causes of issues more efficiently than traditional print-based debugging.

Further reading
---------------

[Python Docs: pdb — The Python Debugger](https://docs.python.org/3/library/pdb.html)
