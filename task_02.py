'''Module providing a function.'''
import pathlib

def get_cats_info(path):
    '''function returns list of cats info'''
    cats_list = []
    try:
        if pathlib.Path.exists(path):
            with open(path, 'r', encoding = 'utf-8') as file:
                for line in file:
                    # remove newline character and split data
                    cat_id, name, age = line.strip().split(',')
                    # append info to the list
                    cats_list.append({"id": cat_id, "name": name, "age": age})
        raise FileNotFoundError

    except FileNotFoundError:
        print(f"The file is not found by the path {path}")
    except Exception as e:
        print(f"Error in file processing: {e}")

    return cats_list