import os
import google.generativeai as genai #Library Function, install this on terminal through pip install google-generativeai
import serial #Library Function through # pip3 install pyserial

genai.configure(api_key="AIza*******************")#Censored API Key, must remake one on Google AI Studio before using this code

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
} #Setting up the genai model (copy paste) Don't worry too much about variables they are some high level ML terms

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
) #Configuring Gemini AI

chat_session = model.start_chat(
  history=[
  ]
)#This array stores history of inputs/outputs through this API Key

while True:
    print("<<Prompting User for input>>") #Debugging Lines (no real significance)
    
    response = chat_session.send_message(input("Ask Gemini Anything: ") + " limit your response to 20 words or less.")
    #This line sends a message to Gemini^

    print("<<Output recieved from gemini>>")

    try:
        #Setting up serial connection to Raspberry Pico, COM5 is for my PC (diff for diff PCs), 115200 baud (bits per second)
        ser = serial.Serial('COM5', 115200, timeout=1)
        print(response.text) #Printing Gemini Response just so we can see
        print("<<Connection to pico is " + (str(ser.is_open)) + ">>") #Is serial connection successful?
        ser.write((response.text + '\n').encode('utf-8'))  #Send the bit sequence followed by newline
        print("<<Output Sent to Pico>>")
        ser.close()
    except Exception as e:
        print(f"Error sending data over serial: {e}")
