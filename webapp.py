import numpy as np
import pickle
import streamlit as st

#loading model
loaded_model=pickle.load(open("D:/project/Crop-Prediction/trained_model.sav",'rb'))

def crop_prediction(input_data):

    input_arr=np.array(input_data)
    inputs_array=input_arr.reshape(1,-1)
    inputs_array

    print("THE CROP IS ")

    if (loaded_model.predict(inputs_array))==0:
        return "APPLE "
    elif(loaded_model.predict(inputs_array))==1:
        return " BANANA "
    elif(loaded_model.predict(inputs_array))==2:
        return " BLACK GRAM"
    elif(loaded_model.predict(inputs_array))==3:
        return "CHICK PEAS"
    elif(loaded_model.predict(inputs_array))==4:
        return " COCONUT"
    elif(loaded_model.predict(inputs_array))==5:
        return " COFFEE "
    elif(loaded_model.predict(inputs_array))==6:
        return " COTTON "
    elif(loaded_model.predict(inputs_array))==7:
        return " GRAPES"
    elif(loaded_model.predict(inputs_array))==8:
        return " JUTE"
    elif(loaded_model.predict(inputs_array))==9:
        return " KIDNEY BEANS "
    elif(loaded_model.predict(inputs_array))==10:
        return " LENTILE"
    elif (loaded_model.predict(inputs_array))==11:
        return "MAIZE "
    elif(loaded_model.predict(inputs_array))==12:
        return "MANGOO "
    elif(loaded_model.predict(inputs_array))==13:
        return " MOTH BEANS "
    elif(loaded_model.predict(inputs_array))==14:
        return " MUNG BEANS"
    elif(loaded_model.predict(inputs_array))==15:
        return "MUSKMELON"
    elif(loaded_model.predict(inputs_array))==16:
        return " ORANGE "
    elif(loaded_model.predict(inputs_array))==17:
        return " PAPAYA "
    elif(loaded_model.predict(inputs_array))==18:
        return " PIGEON PIECE "
    elif(loaded_model.predict(inputs_array))==19:
        return " POMEGRANATE"
    elif(loaded_model.predict(inputs_array))==20:
        return "RICE"
    else:
        return "WATERMELON"
    



def main():

    st.title("CROP PREDICTION")

    N_SOIL=st.number_input("N_SIOL")
    P_SOIL=st.number_input("P_SOIL")
    K_SOIL=st.number_input("K_SOIL")
    TEMPERATURE=st.number_input("TEMPERATURE")
    HUMIDITY=st.number_input("HUMIDITY")
    Ph=st.number_input("PH VALUE")
    RAINFALL=st.number_input("RAIN FALL RATE")
    CROP_PRICE=st.number_input("CROP PRICE")



    diagnosis=""


    if st.button("Crop Prediction Test Result"):
     diagnosis = crop_prediction([N_SOIL,P_SOIL,K_SOIL,TEMPERATURE,HUMIDITY,Ph,RAINFALL,CROP_PRICE])
        
    st.success(diagnosis)


if __name__ == '__main__':
    main()
