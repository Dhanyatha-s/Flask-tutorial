# from flask import Flask
# import os, requests

# app = Flask(__name__)

# @app.route('/', methods = ['GET'])
# def home():
#     url = "https://api.openweathermap.org/data/2.5/weather?q=India&appid ="+ "API key"
#     response = requests.get(url)

#     list_data = response.json()

#     html_data = f"""
#             <table boder = "1">
#             <tr>
#                 <td>Country_code</td>
#                 <td>Coordinates</td>
#                 <td>temp</td>
#                 <td>Pressure</td>
#                 <td>Humidity</td>
#             </tr>
#             <tr>
#                 <td>{str(list_data['sys']['country'])}</td>
#                 <td>{str(list_data['coord']['lon'] + ' ' + str(list_data['coord']['lat']))}</td>
#                 <td>{str(list_data['main']['temp'])}</td>
#                 <td>{str(list_data['main']['pressure'])}</td>
#                 <td>{str(list_data['main']['humidity'])}</td>
#             </tr>

#             </table>
#     """
#     return html_data
# if __name__ == '__main__':
#     app.run(port = 8000,debug=True)



#######################################
from flask import Flask
import os, requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    api_key = "23c34716438e5b1fb776c0c07e7f938c"
    url = f"https://api.openweathermap.org/data/2.5/weather?q=India&appid={api_key}"
    
    response = requests.get(url)

    if response.status_code == 200:  # Check if request was successful
        list_data = response.json()

        # Build HTML table
        html_data = f"""
                <table border="1">
                <tr>
                    <td>Country_code</td>
                    <td>Coordinates</td>
                    <td>Temp (K)</td>
                    <td>Pressure</td>
                    <td>Humidity</td>
                </tr>
                <tr>
                    <td>{str(list_data['sys']['country'])}</td>
                    <td>{str(list_data['coord']['lon'])}, {str(list_data['coord']['lat'])}</td>
                    <td>{str(list_data['main']['temp'])}</td>
                    <td>{str(list_data['main']['pressure'])}</td>
                    <td>{str(list_data['main']['humidity'])}</td>
                </tr>
                </table>
        """
    else:
        # Handle the error gracefully
        html_data = f"<h3>Error: {response.status_code} - {response.json().get('message', 'Unable to fetch data')}</h3>"

    return html_data

if __name__ == '__main__':
    app.run(port=8000, debug=True)
