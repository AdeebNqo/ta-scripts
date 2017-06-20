import csv
import os

def get_tutor_files():
    directory = 'tutor-csv-files'
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

        
def get_marks(filename):
    marks = [item.strip().split(',') for item in open(filename).readlines()]
    return marks

def get_all_marks():
    marks = []
    tutor_files = get_tutor_files()
    for tutor_file in tutor_files:
        marks += get_marks(tutor_file)
    return marks
