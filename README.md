# Python Tables

Python Tables is a module that let's you create and edit tables quickly. 

The Python Table module uses two dimensional lists to provide table like functionality.



## Installation

To install this module, you need to clone the repository to your download folder, (or somewhere else where you can find it again).

```bash
git clone https://github.com/TheCoder777/Python-Tables-New.git
```

 Now you need to copy the tables.py file to the main folder of your project.

```bash
cp ~/downloads/Python-Tables-New/tables.py ~/my_project/
```

For example a structure like this:

```bash
.
├── downloads
│   └── Python-Tables-New
│       ├── LICENSE
│       └── tables.py
└── my_project
    ├── main_file.py
    └── some_file.py
```

Goes to something like this:
```bash
.
├── downloads
│   └── Python-Tables-New
│       ├── LICENSE
│       └── tables.py
└── my_project
    ├── main_file.py
    ├── some_file.py
    └── tables.py
```


Now you can import the module in your main_file.py:

```python
# filename: main_file.py
import tables
```

You successfully installed the module!

Please note that this is only for this one project. For other projects you need to copy the file again!



## Usage

If the installation part was successful and you got no errors on import, you are good to go!



### Reading and counting

Note that in the whole module, you first start with the rows and continue with the columns!

For example:

```python
		[[	'item', 'item', 'item',  'item'	], # row 0
		[	'item', 'item', 'HELLO', 'item'	], # row 1
		[	'item', 'item', 'item',  'item'	]] # row 2
# column	0		1		 2		 3
```

So for example the item 'HELLO' is at the first row and at the second column.

You start counting from the top to bottom, and then from left to right.

Later in the functions, you always give the row as first, and the column as second parameter!



### Create a Table

To create a table, you need to call the 'Table()' function.

```python
import tables

your_table = tables.Table()
```

If you want to give it a height (number of rows), or a length (number of columns) at this point, you can pass this to the function like this:

```python
height = 2
length = 4
your_table = tables.Table(height, length)
```



### Printing a Table

You can easily print your table just by "printing it as it is".

```python
print(your_table)
```

This will print your table in a more Human readable format like this:

```bash
Empty; Empty; Empty; Empty; |
Empty; Empty; Empty; Empty; |
```



You can also show your table, by calling its 'show()' function.

```python
your_table.show()
```

This would output something like this:

```python
['Empty', 'Empty', 'Empty', 'Empty']
['Empty', 'Empty', 'Empty', 'Empty']
```

'Empty' is the default value here.



### Changing and inserting Values

#### Default value:

The default Value can be set by using the 'val' parameter

```python
your_table = tables.Table(val="Hello")
```



#### Filling with values:

To fill your entire table with one value, you can use the 'fill()' function.

```python
your_table.fill("Hello")
```

If you have want to fill the table with a list, the list will be applied to every row.

```python
your_table.fill(["Hello", "Hi"])
```

If the list is too long to fit the table, it will be cut away automatically.



#### Insert values for rows/columns:

You can fill a row or a column with one value:

```python
your_table.fill_row(1, "Hello") # fill row 1

your_table.fill_column(2, "Hi") # fill column 2
```

You can also fill multiple rows/columns at once:

```python
your_table.fill_row([1,2,3], "Hello") # fill rows 1, 2, 3

your_table.fill_column([2,3,4], "Hi") # fill columns 2, 3, 4
```

The same applies if you have a list of values, independent of how many rows/columns you want to fill

```python
your_table.fill_row([1,2,3], ["Hello", "Hi"]) # fill rows 1, 2, 3

your_table.fill_column(2, ["Hello", "Hi"]) # fill column 2
```



#### Insert value(s) at specific position:

To set a value to one specific item in your table, you can use the 'insert()' function:

```python
your_table.insert(2, 1, "Hello!")
```

Of course you can insert a value to different items at once.

The only tricky thing is how you provide the positions right!

You have to put the positions, for example 1,3 and 2,4 in tuples or lists and then put it in a list or in a tuple:

```python
your_table.insert(items=[[1,3], [2,4]], val="Hello!") # lists in list

# also works:
your_table.insert(items=([1,3], [2,4]), val="Hello!") # lists in tuple
your_table.insert(items=[(1,3), (2,4)], val="Hello!") # tuples in list
your_table.insert(items=((1,3), (2,4)), val="Hello!") # tuples in tuple
```

Note that if you use the items list, you should use the 'val' variable to set the value.

If you want to add different values at different positions, you need to give a list with all values to the 'val' parameter:

```python
your_table.insert(items=[[1,3], [2,4]], val=["Hello!", "World!"])
```

This will insert "Hello!" at position [1,3] and "World!" at position [2,4].

Another way to do this is by using the x- and y- coordinates in different lists:

```python
y = [1,2] # all y values (rows)
x = [3,4] # all x values (columns)
your_table.insert(y, x, val=["Hello!", "World!"])
```

Don't worry if one list (x, y, val) is too short or too long. The 'insert()' function will automatically crop it or fill missing values with default values.



### Getting items

#### Get entire table

To get the entire table as a data structure, you can just call the 'get()' function:

```python
data = your_table.get()
```

'data' should look something like this, if you print it:

```python
>>> print(data)
[['Hello', 'Hello', 'Hello', 'Hello'],
['Hello', 'Hello', 'Hello', 'Hello'],
['Hello', 'Hello', 'Hello', 'Hello']]
```



#### Get a specific row or column

To get a specific row/column, you need to give the 'get()' function the 'row'/'column' argument:

```python
third_row = your_table.get(row=2) # returns the second row
second_column = your_table.get(column=1) # returns the first column
```

You can also do this with multiple rows and columns:

```python
rows = your_table.get(row=(2,3)) # row 2,3
columns = your_table.get(column=[1,3]) # column 1,3
```



#### Get specific item(s)

If you need to get a specific item from an exact position, you need the 'items' parameter:

```python
item = your_table.get(items=(1,2)) # item from first row and second column
```

For multiple items, you need to use tuple in list again (or similar):

```python
items = your_table.get(items=[(1,2), (2,2)])
```



### Adding rows and columns

#### Adding rows:

To add a row to your table, you have to call the 'add_row()' function:

```python
your_table.add_row()
```

This will add a row with default values to the last row of your table.

To use a different value, you can use the 'val' parameter:

```python
your_table.add_row(val="Hello")
```

If you want your new row to be at the top, you can use the 'side' parameter:

```python
your_table.add_row(side="Top", val="Hello")
```

You can also place the row at a specific position (y-axis / between two rows) in your table, by using 'pos':

```python
your_table.add_row(pos=3, val="Hello")
```

To choose if the new row goes under or over the current third row, you can use the 'side' parameter again (default value is "Top"), relative to the row 'pos' is pointing to:

```python
your_table.add_row(pos=3, side="Bottom", val="Hello")
```

This will place the new row under the current third row.

And if you want more than one row added at the time, you can use the 'num' parameter:

```python
your_table.add_row(pos=3, side="Bottom", val="Hello", num=4)
```

This will add four new rows under the current third row, with "Hello" as value.

If you don't want to use one value for the entire row, you can just give the 'val' parameter a list or a tuple of values:

```python
your_table.add_row(pos=3, side="Bottom", val=["Hello", "what's", "up?"])
```

This will fill the first three cells with the three values, and then fill up with default values.

If the table has only a length of two, the function will crop the last value away! (The values are inserted from top to bottom!)



#### Adding columns

Adding a column is as simple as adding a row. Just call the 'add_column' function.

```python
your_table.add_column()
```

This will add a new column with default values at the right side of your table.

If you want to use a different value, you can use the 'val' parameter:

```python
your_table.add_column(val="Hello")
```

To add the new column at the left of your table, you should use the 'side' parameter:

```python
your_table.add_column(side="Left", val="Hello")
```

You can also place the new column at a specific position (x-axis / between two columns) in your table, by using the 'pos' parameter as shown below.

```python
your_table.add_column(pos=3, val="Hello")
```

By default this will add the new column at the left side of the current third column.

To change that, use the 'side' parameter again:

```python
your_table.add_column(pos=3, side="Right", val="Hello")
```

Now this will insert the new column at the right side of the current third column.

If you want more than one column added at a time, the 'num' parameter will be your friend!

```python
your_table.add_column(pos=3, side="Right", val="Hello", num=4)
```

This will now add 3 columns at the right side of the current third column, instead of one.

If you need to use more values at a time, you can just give the 'val' parameter a list or a tuple of values:

```python
your_table.add_column(pos=3, side="Right", val=["Hello", "what's", "up?"])
```

Now this will fill the first three cells of the table with the three given values, and then fill the rest with default values. If the table has only a hight of two, it will crop the last value away automatically! (The values are inserted from left to right!)

