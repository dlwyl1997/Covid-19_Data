import pandas as pd
import flask

file_path = "D:/GLA Lessons/MSc Project/Data/PROCESSED_DATA.csv"
app = flask.Flask(__name__)


@app.route("/")
def show_csv():
    """show csv/excel in html"""
    df = pd.read_csv(file_path)

    # TODO: data process

    data_html = df.to_html('D:/GLA Lessons/MSc Project/Project/Covid-19_Data_Analysis/covid19_data_analysis_platform/templates/covid/dataframe.html')

    return f"""
        <html>
            <body>
                <h3>Dataset of Covid-19</h3>
                </div>{data_html}</div>
            </body>
        </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0')
