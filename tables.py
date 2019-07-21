# MIT License
#
# Copyright (c) 2019 TheCoder777
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

## default values
default_len     = 4
default_high    = 8
default_val     = "Empty"

## row object
class row():
    def __init__(self, len=default_high, val=default_val):
        self.len = len
        self.default_val = val
        self.build()


    def build(self):
        if isinstance(self.default_val, (list, tuple)):
            if len(self.default_val) > self.len:
                del self.default_val[self.len:]
            elif len(self.default_val) < self.len:

                diff = self.len - len(self.default_val)
                for i in range(diff):
                    self.default_val.append(default_val)
            self.root = self.default_val
        else:
            self.root = [self.default_val for self.len in range(self.len)]

    def insert(self, pos, val):
        pos = int(pos) # make sure it is an int

        if pos > len(self.root): # check if the position is actually in the row
            print("ERROR:\nNo position '{}' in this row!".format(pos))
            return False
        else:
            self.root[pos] = val
            return True

    def fill(self, val):
        if isinstance(val, (list, tuple)):
            if len(val) > len(self.root):
                print("ERROR:\nThe Provided list of elements is too long to fit the table!")
                return False
            else:
                for i in range(len(val)):
                    self.root[i] = val[i]
        else:
            for i in range(len(self.root)):
                self.root[i] = val
            return True

    def get(self, item=None):
        if item != None:
            if item > len(self.root): # check if the position is actually in the row
                print("ERROR:\nNo position '{}' in this row!".format(pos))
            else:
                return self.root[item]
        else:
            return self.root

    def get_str(self):
        self.root_str = ""
        for item in self.root:
            self.root_str+=str(item)+"; "
        return self.root_str



## Table object
class Table():
    def __init__(self, columns=default_len, rows=default_high, val=default_val):
        # self.row = row(len=rows, val=val) # crate instance of row object#
        ## this would link all instances together and changes all rows at once every time!

        self.side_top = ["TOP", "Top", "top", "T", "t"] # class variable, so it's easyer to change
        self.side_bottom = ["BOTTOM", "Bottom", "bottom", "B", "b"]
        self.side_left = ["LEFT", "Left", "left", "L", "l"]
        self.side_right = ["RIGHT", "Right", "right", "R", "r"]
        self.rows = int(rows)
        self.val = val
        self.columns = int(columns)

        self.build() # finish init with build

    def __str__(self):
        return str(self.show("get_str"))

    def __repr__(self):
        return str(self.show("get_str"))

    def __convert_to_list(self): # convert table to list format
        self.root_list = [] # create list to return
        for row in self.root:
            self.root_list.append(row.get()) # get each element and append it to list
        return self.root_list

    def build(self):
        self.root = [row(len=self.columns, val=self.val) for r in range(self.rows)] # create main table

    def update(self):
        self.rows = len(self.root)
        self.columns = len(self.root[0].get())

    def show(self, method="default"):
        if method == "default":
            for r in self.root: # r for row
                print(r.root)

        elif method == "get_str": # get the list returned as string
            self.root_str = ""
            for r in self.root:
                self.root_str += r.get_str()+"|\n"
            return self.root_str

        else: # default
            print("The method '{}' is not valid!".format(method))

    def get(self, row=None, column=None, items=None):
        if row != None:
            if isinstance(row, (list, tuple)): # if multiple rows are given
                self.get_rows = []
                for i in row:
                    self.get_rows.append(self.root[i].get())
                return self.get_rows
            elif isinstance(row, int): # for singe row
                return self.root[row].get()
        elif column != None:
            self.get_columns = []
            if isinstance(column, (list, tuple)): # if multiple columns are given
                for i in column:
                    for row in self.root:
                        self.get_columns.append(row.get(i))
                    return self.get_columns
            elif isinstance(column, int): # for singe column
                for row in self.root:
                    self.get_columns.append(row.get(column))
                return self.get_columns
        elif items != None:
            if isinstance(items[0], int) and isinstance(items[1], int): # if only one items is given
                return self.root[items[0]].get(item=items[1]) # items is still a list, but with two integers, and no lists inside
            elif isinstance(items, (list, tuple)): # if multiple items are given
                self.get_items = []
                for item in items:
                    if isinstance(item, (list, tuple)):
                        self.get_items.append(self.root[item[0]].get(item[1]))
                    else:
                        print("The postition of an item must be provided in a tuple or in a list.\nOne item has to be in a list as two inters.")
                return self.get_items

        else: # return entire table
            return self.__convert_to_list() # converts the entire table to one list and returns the list

    def fill(self, val):
        if isinstance(val, (list, tuple)):
            if len(val) > self.columns:
                del val[self.columns:]
            for row in self.root:
                row.fill(val)
        else:
            for row in self.root:
                row.fill(val)

    def fill_row(self, row, val): # if multiple rows are given
        if isinstance(row, (list, tuple)):
            for r in row:
                self.root[r].fill(val)
        else: # for singe row
            self.root[row].fill(val)

    def fill_column(self, col, val):
        if isinstance(col, (list, tuple)): # if multiple columns are given
            for c in col:
                for row in self.root:
                    row.insert(c, val)
        else: #  for singel column
            for row in self.root:
                row.insert(col, val)

    def insert(self, row=None, column=None, val=default_val, items=None):
        if items != None and row == None and column == None:
            if isinstance(items, (list, tuple)): # check if 'items' is a list
                if isinstance(items[0], int) and isinstance(items[1], int): # if the position is given in the list/tuple directly
                    self.root[items[0]].insert(items[1], val)
                else:
                    if isinstance(val, (list, tuple)):
                        for v, i in zip(val, items):
                            if isinstance(i, (list, tuple)):
                                self.root[i[0]].insert(i[1], v)
                            else:
                                print("The position of an item must be provgided in a puple or in a list.")
                    else:
                        for i in items:
                            if isinstance(i, (list, tuple)): # if there is a list/tuple in the 'items' list/tuple
                                self.root[i[0]].insert(i[1], val)
                            else:
                                print("The postition of an item must be provided in a tuple or in a list.")
            else:
                print("Multiple items must be provided in a tuple or in a list, with the 'items' argument.")
        elif row != None and column != None:
            if isinstance(row, (list, tuple)) and isinstance(column, (list, tuple)): # row and column are given as lists
                if len(row) > len(column):      # make row and column equal in length
                    diff = len(row) - len(column)
                    del row[diff:]
                elif len(column) > len(row):    # make row and column equal in length
                    diff = len(column) - len(row)
                    del column[diff:]
                # row and col should have an equal length now
                if isinstance(val, (list, tuple)): # if 'val' is a list or tuple (multiple values)
                    if len(val) != len(row) or len(val) != len(column): # if the amount of values is not equal to the lenght of given positions
                        if len(val) > len(row): # make values equal to the length of positions
                            diff = len(val) - len(row)
                            del val[diff:]
                        elif len(val) < len(row): # make values equal to the length of positions
                            diff = len(row) - len(val)
                            for i in range(diff):
                                val.append(default_val)
                        elif len(val) > len(column): # make values equal to the length of positions
                            diff = len(val) - len(column)
                            del val[diff:]
                        elif len(val) < len(column): # make values equal to the length of positions
                            diff = len(column) - len(val)
                            for i in range(diff):
                                val.append(default_val)
                        ## no else, it has to be eqal now

                    if len(val) == len(row) and len(val) == len(column):
                        for v, r, c in zip(val, row, column): # zip to one list to iterate
                            self.root[r].insert(c, v) # insert at given positions with given values
                if not isinstance(val, (list, tuple)): # Value is anything, but not list/tuple. But row and column are still lists/tuples
                    for r, c in zip(row, column): # zip to one list to iterate
                        self.root[r].insert(c, val) # insert at given positions with (default) value
            else:
                self.root[row].insert(column, val) # default insert. Row and column are integers.
        else:
            print("Insert() needs at least one positions to insert in the table.")

    def add_row(self, pos=None, side=None, val=default_val, num=1): # num stands for how many rows
                ## add individual length to each row?
        if pos != None:
            if pos > self.rows:
                print("Postion: '{}' is not in the table!".format(pos))
            else:
                if side != None:
                    if side in self.side_top:
                        for i in range(num):
                            self.root.insert(pos, row(len=self.columns, val=val))
                        self.update()
                    elif side in self.side_bottom:
                        for i in range(num):
                            self.root.insert(pos + 1, row(len=self.columns, val=val))
                        self.update()
                    else:
                        print("Specified side is not available!")
                else:
                    for i in range(num):
                        self.root.insert(pos, row(len=self.columns, val=val))
                    self.update()
        elif side != None:
            if side in self.side_top:
                for i in range(num):
                    self.root.insert(0, row(len=self.columns, val=val))
                self.update()
            elif side in self.side_bottom:
                for i in range(num):
                    self.root.append(row(len=self.columns, val=val))
                self.update()
            else:
                print("Specified side is not available!")
        else:
            for i in range(num):
                self.root.append(row(len=self.columns, val=val))
            self.update()

    def add_column(self, pos=None, side=None, val=default_val, num=1): # num stands for how many rows
        if isinstance(val, (list, tuple)):
            if len(val) > self.rows: # make values equal the hight of the table
                del val[self.rows:]
            elif len(val) < self.rows:
                diff = self.rows - len(val)
                for i in range(diff):
                    val.append(default_val)

            if pos != None:
                if pos > self.columns:
                    print("Postion: '{}' is not in the table!".format(pos))
                else:
                    if side != None:
                        if side in self.side_left:
                            for i in range(num):
                                for row, v in zip(self.root, val):
                                    row.root.insert(pos, v)
                            self.update()
                        elif side in self.side_right:
                            for i in range(num):
                                for row, v in zip(self.root, val):
                                    row.root.insert(pos + 1, v)
                            self.update()
                        else:
                            print("Specified side is not available!")
                    else:
                        for i in range(num):
                            for row, v, in zip(self.root, val):
                                row.root.append(v)
                        self.update()
            elif side != None:
                if side in self.side_left:
                    for i in range(num):
                        for row, v in zip(self.root, val):
                            row.root.insert(0, v)
                    self.update()
                elif side in self.side_right:
                    for i in range(num):
                        for row, v in zip(self.root, val):
                            row.root.append(v)
                    self.update()
                else:
                    print("Specified side is not available!")
        elif pos != None:
            if pos > self.columns:
                print("Postion: '{}' is not in the table!".format(pos))
            else:
                if side != None:
                    if side in self.side_left:
                        for i in range(num):
                            for row in self.root:
                                row.root.insert(pos, val)
                        self.update()
                    elif side in self.side_right:
                        for i in range(num):
                            for row in self.root:
                                row.root.insert(pos + 1, val)
                        self.update()
                    else:
                        print("Specified side is not available!")
                else:
                    for i in range(num):
                        for row in self.root:
                            row.root.insert(pos, val)
                    self.update()
        elif side != None:
            if side in self.side_left:
                for i in range(num):
                    for row in self.root:
                        row.root.insert(0, val)
                self.update()
            elif side in self.side_right:
                for i in range(num):
                    for row in self.root:
                        row.root.append(val)
                self.update()
            else:
                print("Specified side is not available!")
        else:
            for i in range(num):
                for row in self.root:
                    row.root.append(val)
            self.update()
