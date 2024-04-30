'''Module providing a function.'''
import pathlib

def total_salary(path):
    '''returns sum and middle amount of salary'''
    try:
        if pathlib.Path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                salaries = [int(line.split(',')[1]) for line in file.readlines()]
                total = float(sum(salaries)) if salaries else 0
                average = total / len(salaries) if salaries else 0
        
            return total, average
        raise FileNotFoundError

    except FileNotFoundError:
        print(f"The file is not found by the path {path}")
        return 0, 0
    except Exception as e:
        print(f"Error in file processing: {e}")
        return 0, 0
