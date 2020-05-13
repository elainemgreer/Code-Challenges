def snake_to_camel(var_name):


  new_list = var_name.split("_")

  new_string = new_list[0].lower()

  new_list.pop(0)

  for word in new_list:
    new_string += word.title()
  

  return new_string









