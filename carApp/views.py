from django.shortcuts import render
import pickle


def home(request):
    return render(request,"home.html")

def prediction(request):
    file = open("random_forest_regression_model.pkl","rb")
    model = pickle.load(file)
    lis = []
    
    year = int(request.GET["Year"])
    avg_cost_price = float(request.GET["Average_Cost_Price"])
    mileage = float(request.GET["Mileage"])
    seats = int(request.GET["Seats"])
    km_driven = int(request.GET["KM_driven"])
    seller_type = request.GET["Seller_Type"]
    fuel_type = request.GET["Fuel_type"]
    transmission_type = request.GET["Transmission_Type"]

    Age_of_vehicle = 2023-year
        
    if (seller_type=="individual"):
        seller_type_Individual =1
        seller_type_Trustmark_Dealer =0
    elif (seller_type=="Trustmark_dealer"):
        seller_type_Trustmark_Dealer=1
        seller_type_Individual = 0
    else:
        seller_type_Trustmark_Dealer =0
        seller_type_Individual = 0

    if (fuel_type=="Petrol"):
        fuel_type_Petrol = 1
        fuel_type_Diesel = 0
        fuel_type_LPG = 0
    elif(fuel_type=="Diesel"):
        fuel_type_Diesel = 1
        fuel_type_Petrol = 0
        fuel_type_LPG = 0
    elif (fuel_type=="LPG"):
        fuel_type_LPG = 1
        fuel_type_Petrol = 0
        fuel_type_Diesel = 0
    else:
        fuel_type_LPG = 0
        fuel_type_Petrol = 0
        fuel_type_Diesel = 0

    if (transmission_type=="Manual"):
        transmission_type_Manual = 1
    else:
        transmission_type_Manual = 0

        # format of features is same as X in training model
    pred = model.predict([[Age_of_vehicle,km_driven ,mileage,seats,avg_cost_price,seller_type_Individual,seller_type_Trustmark_Dealer,fuel_type_Diesel,fuel_type_LPG,fuel_type_Petrol,transmission_type_Manual]])
    
    output = round(pred[0],2)

    context = {"price":output}

    

    return render(request,"prediction.html",context)