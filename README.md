# Practice with <code>exbook</code> Package

The package <code>exbook</code> is used for practicing basic Python programming. So far there are totally 36 questions with different difficulty levels. For the purpose of practicing, you are recommended to only use basic built-in functions like <code>find()</code>, <code>min()</code>, <code>max()</code> and <code>sum()</code>. Imported packages or more advanced functions or methods, such as <code>sort()</code>, <code>argmin()</code>, or <code>split()</code> should be avoided. 

## Steps of running <code>exbook</code>

### Step 1: import the exercise book


```python
from exbook import book as eb

len(eb)
```




    36



The variable <code>eb</code> is a tuple containing 36 questions.

### Step 2: print questions

Each question can be retrieved by the corresponding indices, and can be printed by the function <code>print()</code>. 


```python
print(eb[0])        # Print the first question
```

    Define a function with two strings to be the input arguments. The output is 
    the summation of the numerical values of the input strings. For example, if 
    the input strings are "3.5"and "2.7", then the output is 6.2, as a floating
    point number.



<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Input1: str</th>
      <th>Input2: str</th>
      <th>Output: float</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Test 1:</th>
      <td>3.5</td>
      <td>2.7</td>
      <td>6.2</td>
    </tr>
  </tbody>
</table>
</div>


    
<b>Data Type Conversion: Easy</b>
    


The printed question information includes: 1) the description of the question; 2) sample inputs and outputs; and 3) the ID and difficulty level of the question.

### Step 3: write a function to solve the question


```python
def dtc(string1, string2):
    
    return float(string1) + float(string2)
```

### Step 4: check the correctness of the question

The <code>exbook</code> package checks the correctness of the user-defined functions by a number of hidden tests. These tests can be run by the method <code>check()</code>. 


```python
eb[0].check(dtc)
```

    You passed 3 of the 3 tests. 
    The solution is correct


In case you want to know what is wrong with the tests, you may specify the argument <code>cheat=True</code> to show the results of these hidden tests.


```python
eb[0].check(dtc, cheat=True)
```


<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Input 1: str</th>
      <th>Input 2: str</th>
      <th>Your output</th>
      <th>Correct output: float</th>
      <th>Correct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Test 1:</th>
      <td>3.5</td>
      <td>2.7</td>
      <td>6.2</td>
      <td>6.2</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Test 2:</th>
      <td>1.2</td>
      <td>5</td>
      <td>6.2</td>
      <td>6.2</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Test 3:</th>
      <td>2</td>
      <td>4</td>
      <td>6.0</td>
      <td>6</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>


    You passed 3 of the 3 tests. 
    The solution is correct

