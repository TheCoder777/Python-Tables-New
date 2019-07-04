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



### Create a Table

To create a table, you need to call the '.Table()' function.

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

This will print your table in a Human readable format like this:

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



#### Insert value(s) at specific position:

To set a value to one specific item in your table, you can use the 'insert()' function:

```python
your_table.insert(2, 1, "Hello!")
```

Of course you can insert a value to different items at once.

The only tricky thing is how you provide the positions right!

You have to put the positions, for example 1, 3 and 2,4, in tuples or lists and then put it in a list or in a tuple:

```python
your_table.insert(items=[[1,3], [2,4]], val="Hello!") # lists in list

# also works:
your_table.insert(items=([1,3], [2,4]), val="Hello!") # lists in tuple
your_table.insert(items=[(1,3), (2,4)], val="Hello!") # tuples in list
your_table.insert(items=((1,3), (2,4)), val="Hello!") # tuples in tuple

```

Note that if you use the items list, you should use the 'val' variable to set the value.



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
third_row = your_table.get(row=2) # returns the third row
second_column = your_table.get(column=1) # returns the second column
```

You can also do this with multiple rows and columns:

```python
rows = your_table.get(row=(2,3)) # row 2,3
columns = your_table.get(column=[1,3]) # column 1,3
```

#### Get specific item(s)

If you need to get a specific item from an exact position, you need the 'items' parameter:

```python
item = your_table.get(items=(1,2)) # item from second column and third row
```

For multiple items, you need to use tuple in list again (or similar):

```python
items = your_table.get(items=[(1,2), (2,2)])
```

