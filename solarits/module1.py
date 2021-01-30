from flask import Flask
import json
app = Flask(__name__)


@app.route('/')
@app.route('/generate')
def generate():
    # Render the page
    
    f=open('D:\Visual studio\solarits solution\solarits\page.json','r')
    y = json.loads(f.read())
    f.close()
    length=len(y['Attributes'])
    string=''
    for i in range(0, length):
        if y['Attributes'][i]['Type']=='TextBox':
            string+=y['Attributes'][i]['Name'] + '  ' + '<input type=textbox maxlength='+y['Attributes'][i]['Size'] + '> <br> '
        elif y['Attributes'][i]['Type']=='SecretTextBox':
             string+=y['Attributes'][i]['Name'] + '  ' + '<input type=password maxlength='+y['Attributes'][i]['Size'] + '> <br> '
        elif y['Attributes'][i]['Type']=='Dropdown':
             string+=y['Attributes'][i]['Name']+'  '+'<select id='+y['Attributes'][i]['Type']+'><option value='+y['Attributes'][i]['DropdownValues'][0]['Value']+'>'+y['Attributes'][i]['DropdownValues'][0]['DisplayValue']+'</option><option value='+y['Attributes'][i]['DropdownValues'][1]['Value']+'>'+y['Attributes'][i]['DropdownValues'][1]['DisplayValue']+'</option></select><br>'
    string+='<button>'+y['ActionDisplayName']+'</button>'
    return string

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)

