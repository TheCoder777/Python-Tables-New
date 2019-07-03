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
    def __init__(self, len=default_len, val=default_val):
        self.len = len
        self.default_val = val
        self.build()


    def build(self):
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
        for i in range(len(self.root)):
            self.root[i] = val
        return True

    def get(self, item=False):
        if item != False or item == 0: # if position is 0
            item = int(item) # make sure it is an int
            if item > len(self.root): # check if the position is actually in the row
                print("ERROR:\nNo position '{}' in this row!".format(pos))
            else:
                return self.root[item]
        else:
            return self.root

    def get_str(self):
        self.root_str = ""
        for item in self.root:
            self.root_str+=item+"; "
        return self.root_str



## Table object
class Table():
    def __init__(self, columns=default_high, rows=default_len, val=default_val):
        # self.row = row(len=rows, val=val) # crate instance of row object#
        ## this would link all instances together and changes all rows at once every time!

        self.rows=rows
        self.val = val
        self.columns = int(columns)

        self.build() # finish init with build

    def __str__(self):
        return str(self.show("get_str"))

    def __repr__(self):
        return str(self.show("get_str"))

    def __convert_to_list(self):
        self.root_list = [] # create list to return
        for row in self.root:
            self.root_list.append(row.get()) # get each element and append it to list
        return self.root_list

    def build(self):
        self.root = [row(len=self.rows, val=self.val) for col in range(self.columns)] # create main table

    def show(self, method="default"):
        if method == "default":
            for r in self.root: # r for row
                print(r.root)

        elif method == "get_str": # get the list returned as string
            self.root_str = ""
            for i in self.root:
                self.root_str += i.get_str()+"|\n"
            return self.root_str

        else: # default
            print("The method '{}' is not valid!".format(method))

    def get(self, row=False, column=False, items=False):
        if row:
            if isinstance(row, (list, tuple)): # if multiple rows are given
                self.get_rows = []
                for i in row:
                    self.get_rows.append(self.root[i].get())
                return self.get_rows
            elif isinstance(row, int): # for singe row
                return self.root[row].get()
        elif column:
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
        elif items:
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

    def insert(self, row=False, col=False, val=False, items=False, ):
        if items != False and row == False and col == False:
            if isinstance(items, (list, tuple)):
                for i in items:
                    if isinstance(i, (list, tuple)):
                        self.root[i[0]].insert(i[1], val)
                    else:
                        print("The postition of an item must be provided in a tuple or in a list.")
            else:
                print("Multiple items must be provided in a tuple or in a list.")

        else:
            self.root[row].insert(col, val)
