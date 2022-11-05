# to keep track of current items in the shopping list
items = []


def clear(file):
  # move the file pointer to the top
  file.seek(0)

  # clear its contents
  file.truncate()


def create(file_name):
  file = open(f"{file_name}.txt", "w")
  return file


def add_item(item, file):
  file.write(f'{item}\n')
  items.append(item)


def remove_item(item, file):
  clear()  # clear file contents
  items.remove(item)

  for item in items:
    file.write(f'{item}\n')
  file.close()


s_list_name = input("Enter a name for your list: ")

# Create shopping list
file = create(s_list_name)

# Add Items
add_item('tomato', file)
add_item('potato', file)
add_item('spinach', file)
add_item('bread', file)
add_item('apple', file)
file.close()

remove_item('bread', file)
