import re
import sys

def extract_headers(html_content):
    titles = re.findall(r'<title>(.*?)</title>', html_content, re.S)
    headers = re.findall(r'<h\d.*?>(.*?)</h\d>', html_content, re.S)
    return titles, headers

def main():
    if len(sys.argv) != 2:
        print("Usage: python hextractor.py <filename>")
        return

    filename = sys.argv[1]
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            html_content = file.read()
            
            titles, headers = extract_headers(html_content)

            if titles:
                print(titles[0])

            for header in headers:
                print(header.strip())

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()