# Day-72-Count-Words-and-Characters

Day 72/100 - Python Program to Count the Number of Words and Characters in a String

# Count Words and Characters in a String

A program to dynamically calculate both the total character count and the total word count of a user-provided string using Python's built-in string methods.

## 📝 Description

This program analyzes a string of text inputted by the user and extracts two key metrics: the total number of characters (including spaces) and the total number of discrete words.

The logic is housed within the `count_words_and_characters(input_string)` function. To find the character count, the script simply applies Python's built-in `len()` function directly to the raw input string, which inherently counts every letter, number, space, and punctuation mark. To find the word count, it utilizes the `.split()` string method. By default, `.split()` separates a string into a list of substrings based on any whitespace. The script then uses `len()` on this newly generated list to accurately tally the total number of words. Finally, the function returns both integer values as a tuple, which are unpacked and cleanly printed to the console.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A string of text provided by the user via the terminal prompt.



### Output:

* A formatted string stating: "Number of words: [num_words]".


* A formatted string stating: "Number of characters (including spaces): [num_characters]".



### Rules:

1. The program must accept a string input from the user.


2. The core logic must be encapsulated in a function named `count_words_and_characters(input_string)`.


3. The function must calculate the total characters using `len(input_string)`.


4. The function must calculate the total words by evaluating `len(input_string.split())`.


5. The function must return both counts, and the driver code must capture and print them on separate lines.



---

## 💡 Examples

### Example 1 (Standard Sentence)

**Input:**

```text
Hello world from Python

```

**Output:**

```text
Number of words: 4
Number of characters (including spaces): 23

```

**Explanation:** The `.split()` method breaks the string into `['Hello', 'world', 'from', 'Python']`, resulting in a length of 4. The character count tallies all letters plus the 3 spaces between the words, resulting in 23.

### Example 2 (Extra Whitespace)

**Input:**

```text
  Data   Science  

```

**Output:**

```text
Number of words: 2
Number of characters (including spaces): 16

```

**Explanation:** Even with trailing, leading, and multiple internal spaces, the `.split()` method smartly groups consecutive whitespaces as a single delimiter, correctly returning 2 words ("Data" and "Science"). The character count, however, includes every single space typed, returning 16.

### Example 3 (Empty String)

**Input:**

```text


```

*(User presses Enter without typing anything)*

**Output:**

```text
Number of words: 0
Number of characters (including spaces): 0

```

**Explanation:** An empty string has 0 characters. Attempting to split an empty string results in an empty list `[]`, which has a length of 0.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script as "Day 72.py").

```bash
git clone https://github.com/adiaryaz/Day-72-Count-Words-and-Characters.git
cd count-words-and-characters

```

2. **Run the program**:

```bash
python "Day 72.py"

```

Enter any word, sentence, or paragraph when prompted to instantly see its exact word and character footprint!
