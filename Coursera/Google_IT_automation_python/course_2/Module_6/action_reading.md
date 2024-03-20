IT skills in action reading
===========================

Congratulations! You have gained so much knowledge about using Python to interact with your operating system. There are many technical pieces that are included while using regexes in your code, but how would you apply the skills you learned in a professional setting?

In this reading, you will review an example of how regular expressions are used in the real world.

**Disclaimer:** The following scenario is based on a fictitious company called LogicLink Innovations.

Time is ticking
---------------

Dakota is a fairly new programmer with his company. He just earned a spot on the project for LogicLink Innovations. This is one of the biggest and most credible companies in the industry, so Dakota knows he has to excel on this project to help make a name for himself. LogicLink Innovations manages customer data and has hundreds of customer phone numbers in its database. The phone numbers are in inconsistent formats. Some are written with dashes, some in parentheses with spaces, and some are just digits. Dakota sees this:

>123-456-7890
>
>(123) 456-7890
>
>1234567890

Dakota is assigned to take the dataset containing phone numbers and organize the formatting so they are all consistent. His manager tells him they need it by the end of the week! There is no way Dakota can work through and edit hundreds of phone numbers. There has to be another way.

Search and replace
------------------

Dakota remembers reading about how other programmers use regular expressions to make their coding life easier. He knows there has to be one that can help him with his dilemma. This can’t be the first time a programmer needs to standardize numbers! He decides to craft a regular expression that captures three groups of digits, each of which might be surrounded by non-digit characters.

Using a regex tool and the sample data from above, he eventually comes up with a regex that matches all three samples:

`^\\D\*(\\d{3})\\D\*(\\d{3})\\D\*(\\d{4})$`

Let’s break down this line of code, piece by piece:

`^\\D\*`

This part of the code matches zero or more non-digit characters at the beginning of the string.

`(\\d{3})`

This part of the code captures exactly three digits, which represent the area code.

`\\D\*`
This part of the code matches zero or more non-digit characters between the area code and exchange.

`(\\d{3} )`

This part of the code captures the three-digit exchange.

`\\D\*`

This part of the code matches zero or more non-digit characters between the exchange and line.

`(\\d{4})$`

This part of the code captures exactly four digits at the end of the string.

Now he has three capture groups: area code, exchange, and number. He then substitutes those groups into a new string using backreferences:

`(\\1) \\2-\\3`

This puts all of the phone numbers into a uniform format.

This regular expression helps Dakota by searching for phone numbers in different formats and replacing them to match the format that Dakota’s manager needs: (123) 456-7890. Dakota begins to code.

He writes up a simple Python script to read the dataset from a file and output the corrected phone numbers using his regular expressions:

```python
import re

with open("data/phones.csv", "r") as phones:

 for phone in phones:

   new\_phone = re.sub(r"^\\D\*(\\d{3})\\D\*(\\d{3})\\D\*(\\d{4})$", r"(\\1) \\2-\\3", phone)

   print(new\_phone)

(123) 456-7890

(123) 456-7890

(123) 456-7890
```

Success! Dakota gets the project done in a single day and is now the office hero. 

A happy client
--------------

By using a regular expression, Dakota expedited the process of collecting, organizing, and providing LogicLink Innovation with its customers’ phone numbers, all in the same format. 

Mark as completedGo to next item