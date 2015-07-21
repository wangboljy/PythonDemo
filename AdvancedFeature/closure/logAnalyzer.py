import os
import sys

class LogAnalyzer(object):
	def __init__(self, dirname):
		self.__dirname = dirname
		self.__report = dict()
		self.__SECTION_DELIMITER = "--------"

		self.__filenum = 0
	
	def analyze(self):
		for root, dirs, files in os.walk(self.__dirname):
			for filename in files:
				self.__analyzeFile(os.path.join(root,filename))
				self.__filenum += 1
	
	def __analyzeFile(self, filename):
		print(">>> analyzing: ", filename)
		envName = None
		client = None
		operation = None

		# closure of report
		def report():
			def getVal(env, client):
				if env:
					return env
				return client
			val = getVal(envName, client)
			if operation not in self.__report:
				self.__report[operation] = set()
			self.__report[operation].add(val)

		# closure for parsing if line contains targets
		def parseVal(line):
			if '=' not in line:
				return
			nonlocal operation
			nonlocal envName
			nonlocal client
			val = line.split('=')[1]
			if "Operation" in line:
				operation = val
			elif "EnvName" in line:
				envName = val
			elif "ClientProgram" in line:
				client = val
			

		with open(filename) as file:
			line = None
			while True:
				line = file.readline().strip()
				if not line:
					break # end of file, exit to analyze next file
				# --- is a section. clear state of section
				if self.__SECTION_DELIMITER in line:
					if operation:
						report()
					envName = None
					program = None
					client = None
					continue
				# analyze data inside this section
				parseVal(line)

			# flush the last part
			report()
						
			print(">>> analysis done in file:", filename)

	def __str__(self):
		ret = ">>> Here's the analysis result\n"
		ret += "analyzed file number: %s\n" % self.__filenum
		ret += "operation number: %s\n" % len(self.__report)
		ret += "\n"
		ret += "operation analysis breakdown\n"
		for operation in self.__report:
			ret += "\t Operation name: %s, client num: %s\n" % (operation, len(self.__report[operation]))
			ret +="\t clients: %s\n" % str(self.__report[operation])
		return ret

if __name__ == '__main__':
	#input your dir or file
	#LogAnalyzer("/home/wangboo/myzone/python/SellerCSSessionServiceLog/").analyze()
	print(sys.argv[1])
	analyzer = LogAnalyzer(sys.argv[1])
	analyzer.analyze()
	print(analyzer)
