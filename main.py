import os
from pyPdf import PdfFileReader, PdfFileWriter

def get_files(directory):
	file_paths = []
	for root, directories, files in os.walk(directory):
			for filename in files:
				filepath = os.path.join(root, filename)
				if filepath.endswith('.pdf'):
					file_paths.append(filepath)
	return file_paths
	
def get_num_pages(filepath):
	pdf = PdfFileReader(open(filepath,'rb'))
	return pdf.getNumPages()

def get_slice_intervals(filepath):
	intervals = []
	num_pages = get_num_pages(filepath)
	left = 0
	pages = 5
	right = pages
	while right <= num_pages:
		intervals.append((left, right))
		if right%pages==0:
			left = right
			right += pages
	return intervals
	
def slice_pdf(filepath):
	names = filepath.split(os.sep)
	actual_filename = names[len(names)-1].replace('.pdf','')
	
	inputpdf = PdfFileReader(open(filepath, "rb"))
	intervals = get_slice_intervals(filepath)
	for interval in intervals:
		output = PdfFileWriter()
		left = interval[0]
		right = interval[1]
		while left < right:
			output.addPage(inputpdf.getPage(left).rotateClockwise(180))
			left+=1
		with open("./tmp/{0}-{1}.pdf".format(actual_filename, left), "wb") as outputStream:
			output.write(outputStream)
			
def get_marks():
	path = './final-labeled'
	files = os.listdir(path)
	for f in files:
		details = f.replace('.pdf','').split('-')
		print '{0},{1}'.format(details[0], details[1])
