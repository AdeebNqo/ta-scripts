from csv_util import *

def create_joined_tutor_list():
    filename = 'final-joined-tutor-marks.csv'
    f = open(filename, 'w+')
    f.write('Campus ID,Mark\n')
    for mark in get_all_marks():
        f.write('{0},{1}\n'.format(mark[0].upper(), mark[1]))
    f.close()
    
if __name__=='__main__':
    create_joined_tutor_list()
