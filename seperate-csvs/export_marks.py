from csv_util import *


def get_mark_by_student_id(campus_id):
    marks = get_all_marks()
    for mark in marks:
        if mark[0]==campus_id.upper():
            return mark
    return None

def export_final_marks():
    output_file = 'Final-Marks.csv'
    input_filename = 'Vula-Template-File.csv'
    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(open(output_file,'w+'), fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            campus_id = row['Campus ID']
            mark = get_mark_by_student_id(campus_id)
            if mark:
                row['Grade'] = mark[1]
            writer.writerow(row)
            
if __name__=='__main__':
    export_final_marks()
