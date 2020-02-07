# Python Exercise Package

## An example of using <code>exbook</code>

The package <code>exbook</code> contains a number of coding exercise questions for you to practice. It can check your solution via a series of tests. You may follow the following steps to use <code>exbook</code>.
1. Install the package via running <b>pip install exbook</b>.

2. Import the package by the following code.


```python
from exbook import book as eb  # Import the exercise book from the exbook package
```

3. After importing the exercise book, we can use <code>eb[i]</code> to access each question in the exercise book. For example, the following code print the description of the first question <code>eb[0]</code>.


```python
eb[0]
```

    Example(s):



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Input1</th>
      <th>Input2</th>
      <th>Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>3.5</td>
      <td>2.7</td>
      <td>6.2</td>
    </tr>
  </tbody>
</table>
</div>





    Define a function with two strings to be the input arguments. The output is the summation of the numerical values of the input strings. For example, if the inputs are "3.5" and "2.7", then the output is 6.2.
    [1mLevel:[0;0m easy



4. You need to write a function according to the question description. 


```python
"""Solution to the question"""
def sum_str(a, b):              # The function as the solution
    return float(a) + float(b)  # Return the summation of numerical values
```

5. The last step is to run the method <code>check</code> of the question <code>eb[0]</code>, then <code>exbook</code> would use a number of tests to check if your function is the correct solution to the exercise question.


```python
# Check if the function "sum_str" is a correct solution 

eb[0].check(sum_str)            
```

    You passed 3 of the 3 tests. 
    The solution is correct


If you cannot figure out the correct answer, you may set the argument <code>cheat</code> of the function <code>check</code> to be <code>True</code>, to display the information on why your solution is wrong.


```python
# Check the function "sum_str" and display the correct solutions

eb[0].check(sum_str, cheat=True)   
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Input1</th>
      <th>Input2</th>
      <th>Your output</th>
      <th>Correct output</th>
      <th>Correct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>3.5</td>
      <td>2.7</td>
      <td>6.2</td>
      <td>6.2</td>
      <td>True</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1.2</td>
      <td>5</td>
      <td>6.2</td>
      <td>6.2</td>
      <td>True</td>
    </tr>
    <tr>
      <td>2</td>
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


There are totally 30 questions with different levels of difficulties in the module. You may now work on the other questions.


```python
len(eb)

eb[1]
```

    Example(s):



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Input1</th>
      <th>Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>151</td>
      <td>True</td>
    </tr>
    <tr>
      <td>1</td>
      <td>-5</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>





    Write a function to determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward. For example, 121 is a palindrome so the output is True, 10 is not a palindrome so the output is False.
    [1mLevel:[0;0m easy




```python
len(eb)
```




    30


