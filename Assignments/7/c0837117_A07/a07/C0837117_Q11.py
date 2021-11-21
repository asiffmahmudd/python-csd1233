# Assignment 07
# c0837117 - Asif Mahmud
# Question 11
# Date of submission: 2021-11-21

def get_input():
    name = input("Enter your name: ")
    description = input("Describe yourself: ")
    return name,description

def make_page(name, description):
    webpage = '''
                <html>
                <head>
                </head>
                <body>
                    <center>
                        <h1>'''+name+'''</h1>
                    </center>
                    <hr />
                    '''+description+'''
                    <hr />
                </body>
                </html>
            '''
    return webpage

if __name__ == '__main__':
    name, description = get_input()
    webpage = make_page(name, description)
    print(webpage)