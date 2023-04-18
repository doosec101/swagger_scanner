# swagger_scanner
This tool checks if the given Url/File has Swagger Ui, That can be tested later for DomXSS....

## What is Swagger Ui?
Swagger UI is a really common library used to display API specifications in a nice-looking UI used by almost every company.

## Clone & Usage

1. git clone https://github.com/doosec101/swagger_scanner
2. cd swagger_scanner
3. pip3 install -r requirements.txt
4. python3 swagger.py -u https://example.com 

**Some Usages**

- python3 swagger.py -u https://example.com -v -o output.txt
- python3 swagger.py -f file_of_urls.txt
- python3 swagger.py -f file_of_urls.txt -v -o output.txt

**Dorks:-**

- Shodan: http.title:"Swagger Ui"
- Google: intext:"Swagger UI" intitle:"Swagger UI" site:yourarget.com
