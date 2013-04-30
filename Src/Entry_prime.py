from Constants import *
from Utility import *
from WebPageSimilarity import *
C:\Program Files\PC Connectivity Solution\;C:\Program Files\PHP\;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;c:\Program Files\Common Files\Roxio Shared\DLLShared\;C:\Program Files\Microsoft SQL Server\100\Tools\Binn\;C:\Program Files\Microsoft SQL Server\100\DTS\Binn\;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\MySQL\MySQL Server 5.5\bin;C:\Program Files\Heroku;C:\Program Files\git\bin;C:\Program Files\git\cmd;C:\Program Files\TortoiseGit\bin;C:\MinGW\bin;C:\MinGW\msys\1.0\bin\;C:\Python33;C:\Program Files\Microsoft\Web Platform Installer\;c:\Program Files\Microsoft ASP.NET\ASP.NET Web Pages\v1.0\
def main():
  
	userURLDirPath =Constants.userProvidedURLFilePath
	if os.path.exists(userURLDirPath):
		f = open(userURLDirPath,"rb")
		urls = f.readline()
		webPageSim = WebPageSimilarity()
		utility =Utility()
		userSite1 = urls.split('|')[0].strip()
		userSite2 = urls.split('|')[1].strip()
		calculatedSimList = webPageSim.calculateUserSim(userSite1,userSite2)
		totalVal=0
		f1= open(Constants.resultFileName,"wb")
		for sim in calculatedSimList:
			f1.write('%f\n' %(sim))
			
			#print sim,":", calculatedSimDict[sim]
			#f1.write('%f\n' %(calculatedSimDict[sim]))
			totalVal += sim
		finalSim = totalVal/4.0
		f1.write('%f' %(finalSim))
		f1.close()
		f.close()
		f2 = open("testSomething.txt","wb")
		
		f2.write("ho gaya")
		f1.close()
		f.close()
		f2.close()
		
		
if __name__ == '__main__':
  main()
  
