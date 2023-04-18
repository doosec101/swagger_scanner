import requests
from optparse import OptionParser
from httpx import get
requests.packages.urllib3.disable_warnings()
from termcolor import colored
import bs4

parser = OptionParser()
parser.add_option("-u", "--url", dest="url",help="Url to scan.", metavar="URL")
parser.add_option("-f", "--file", dest="file",help="File to scan", metavar="FILE")
parser.add_option("-v", "--verbose", dest="verbose",help="Showing the entered url", metavar="VERBOSE",action="store_true")
parser.add_option("-o", "--output", dest="output",help="Save the result to a file", metavar="OUTPUT")
(options, args) = parser.parse_args()
url=options.url
file=options.file
verbose=options.verbose
output=options.output

def check_url():
    if url:
        if verbose:
            print(url)
        else:
            pass
        with open('list.txt','r') as slist:
            for line in slist:
                line=line.strip()
                path=url+"/"+line
                try:
                    response = get(path,verify=False)
                except Exception:
                    pass
                html = bs4.BeautifulSoup(response.text,"lxml")
                title=str(html.title)
                if "Swagger" in title:
                    print(colored("[+] Swagger UI detected at " + path,'blue'))
                    if output:
                        with open(output,"a") as file:
                            file.writelines(path)
                            file.write("\n")
                            file.close()

check_url()

def check_file():
    if file:
        with open(file) as read:
            for line in read:
                line=line.strip()
                if verbose:
                    print(line)
                else:
                    pass
                with open('list.txt') as slist:
                    for line1 in slist:
                        line1=line1.strip()
                        path=line+"/"+line1
                        try:
                            response = get(path,verify=False)
                        except Exception:
                            pass
                        try:
                            html = bs4.BeautifulSoup(response.text,"html.parser")
                            title=str(html.title)
                        except Exception:
                            pass
                       
                        if "Swagger" in title:
                            print(colored("[+] Swagger UI detected at " + path,'blue'))
                            if output:
                                with open(output,"a") as out:
                                    out.writelines(path)
                                    out.write("\n")
                                    out.close()
check_file()
