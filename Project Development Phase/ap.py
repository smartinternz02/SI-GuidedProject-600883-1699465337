
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
app = Flask(__name__)

# Load the model from the pickle file
model = pickle.load(open("db_prediction.pkl",'rb'))

@app.route('/')
def start():
    return render_template('index.html')    

@app.route("/login", methods=['POST'])
def login():
    Sex = request.form['Sex']
    if (Sex=='Male'):
        Sex=1
    else:
        Sex=0    

    #name= request.form['name']

    HighBP = request.form['HighBP']
    if (HighBP=='yes'):
        HighBP=1
    else:
        HighBP=0 

    Fruits = request.form['Fruits']
    if (Fruits=='yes'):
        Fruits=1
    else:
        Fruits=0

    Veggies = request.form['Veggies']
    if (Veggies=='yes'):
        Veggies=1
    else:
        Veggies=0

    AnyHealthcare = request.form['AnyHealthcare']
    if (AnyHealthcare=='yes'):
        AnyHealthcare=1
    else:
        AnyHealthcare=0    

    Highchol =request.form['Highchol']
    if (Highchol=='yes'):
        Highchol=1
    else:
        Highchol=0

    Age= request.form['Age']
    if (Age=='1'):
        Age=1
    elif (Age=='2'):
        Age=2
    elif (Age=='3'):
        Age=3
    elif (Age=='4'):
        Age=4
    elif (Age=='5'):
        Age=5
    elif (Age=='6'):
        Age=6
    elif (Age=='7'):
        Age=7
    elif (Age=='8'):
        Age=8
    elif (Age=='9'):
        Age=9
    elif (Age=='10'):
        Age=10
    elif (Age=='11'):
        Age=11
    elif (Age=='12'): 
        Age=12               
    else:
        Age=13

    BMI = request.form['BMI']

    Smoker = request.form['Smoker']
    if (Smoker=='yes'):
        Smoker=1
    else:
        Smoker=0

    CholCheck = request.form['CholCheck']
    if (CholCheck=='yes'):
        CholCheck=1
    else:
        CholCheck=0            

    Stroke = request.form['Stroke']
    if (Stroke=='yes'):
        Stroke=1
    else:
        Stroke=0

    HvyAlcoholConsump= request.form['HvyAlcoholConsump']
    if (HvyAlcoholConsump=='yes'):
        HvyAlcoholConsump=1
    else:
        HvyAlcoholConsump=0

    Diffwalk= request.form['Diffwalk']
    if (Diffwalk=='yes'):
        Diffwalk=1
    else:
        Diffwalk=0

    HeartDiseaseorAttack = request.form['HeartDiseaseorAttack']
    if (HeartDiseaseorAttack=='yes'):
        HeartDiseaseorAttack=1
    else:
        HeartDiseaseorAttack=0

    PhysActivity= request.form['PhysActivity']
    if (PhysActivity=='yes'):
        PhysActivity=1
    else:
        PhysActivity=0

    NoDocbcCost = request.form['NoDocbcCost']
    if (NoDocbcCost=='yes'):
        NoDocbcCost=1
    else:
        NoDocbcCost=0

    GenHlth =request.form['GenHlth']
    if (GenHlth=='1'):
        GenHlth=1
    elif (GenHlth=='2'):
        GenHlth=2
    elif (GenHlth=='3'):
        GenHlth=3
    elif (GenHlth=='4'):
        GenHlth=4
    else:
        GenHlth=5

    MentHlth = request.form['MentHlth']
    PhysHlth =request.form['PhysHlth']

    Education =request.form['Education']
    if (Education=='1'):
        Education=1
    elif (Education=='2'):
        Education=2
    elif (Education=='3'):
        Education=3
    elif (Education=='4'):
        Education=4
    else:
        Education=5           

    Income =request.form['Income']
    if (Income=='1'):
        Income=1
    elif (Income=='2'):
        Income=2
    elif (Income=='3'):
        Income=3
    elif (Income=='4'):
        Income=4
    elif (Income=='5'):
        Income=5
    elif (Income=='6'):
        Income=6
    elif (Income=='7'):
        Income=7            
    else:
        Income=8    
    


    input_data =[[float(HighBP) ,float(Highchol) , float(CholCheck),float(BMI),float(Smoker),float(Stroke),float(HeartDiseaseorAttack),float(PhysActivity),float(Fruits),float(Veggies), float(HvyAlcoholConsump), float(AnyHealthcare), float(NoDocbcCost), float(GenHlth),float(PhysHlth),float(MentHlth),float(Diffwalk),float(Sex),float(Age),float(Education),float(Income) ]]

    output= model.predict(input_data)
    
    if (output == 0):
        return render_template('result.html', result='Good News, Diabetes not present',rec="According to our prediction model, there is currently no indication that you have diabetes. However, it's important to view this as a snapshot, and maintaining a healthy lifestyle is key to ongoing well-being.",rec1="To continue minimizing the risk of diabetes, we recommend staying active, eating a balanced diet rich in fruits and vegetables, and maintaining a healthy weight. Regular exercise and a nutritious diet contribute to overall health and well-being.")
    elif (output == 1):
        return render_template('result.html', result='there is a risk of getting diabetes',rec="Our analysis suggests that there is a potential risk for developing diabetes in the future. It's essential to understand that this is not a definite prediction but an indication to be mindful of your health.",rec1="To reduce the risk of developing diabetes, consider adopting preventive measures. Focus on maintaining a balanced diet, engaging in regular physical activity, and scheduling routine health check-ups. These lifestyle changes can play a significant role in minimizing the risk.")
    else:
        return render_template('result.html', result='Oh no! you are sufferning from diabetes.',rec="Based on our analysis, it appears that you currently have diabetes. We understand that this may be concerning, but it's important not to panic. This prediction is not a diagnosis, and we strongly recommend consulting with a healthcare professional for a comprehensive evaluation.",rec1="To address this concern promptly, we recommend scheduling a check-up with your healthcare provider. They can provide personalized advice and guidance. Additionally, consider making immediate lifestyle changes such as adjusting your diet and incorporating regular exercise into your routine.")   
        

if __name__ == '__main__':
    app.run(debug=True)