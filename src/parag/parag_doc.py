import os

from mammoth     import convert_to_html
from bs4         import BeautifulSoup

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""
class Parag_Docx_Interpretor(object):


	def __init__(self,path):

		self.path_doc  = path
		self.path_html = self.__get_html_path()
		self.data      = ""

	def read(self):

		self.__convert()

		_html = BeautifulSoup(self.data,'html.parser')

		_questions = self.__get_questions(_html)	

	def __get_questions(self,html):

		_questions = []

		_html_lis = html.find_all('li')

		for _html_li in _html_lis:

			_inner_lis = _html_li.find_all("li")

			if len(_inner_lis) > 0:

				_questions.append(_html_li)

		return _questions

	def __get_html_path(self):

		_dir_doc, _file_doc = os.path.split(self.path_doc)

		_file_html = os.path.splitext(_file_doc)[0]

		return os.path.join(_dir_doc,"%s.html" % (_file_html,))

	def __convert(self):

		_doc  = open(self.path_doc, 'rb')
		self.data  = convert_to_html(_doc)
		self.data  = self.data.value
		_doc.close()

"""*************************************************************************************************
****************************************************************************************************
*************************************************************************************************"""

_path = r"d:\projects\paragliding\src\docs\debug.docx"

_doc = Parag_Docx_Interpretor(_path)

_doc.read()