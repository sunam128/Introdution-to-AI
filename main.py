#function to configure the chatbot's response
def response(user_input):
    #normalize the user input
    user_input=user_input.lower()
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I assist you?"
    elif "how are you" in user_input:
        return "(●'◡'●)(❁´◡`❁)I am doing well" 
    elif "name" in user_input:
        return "my name is chatrtm🐾!"
    elif "weather" in user_input:
        return "I have not been programmed to understand weather yet."
    elif"age" in user_input:
        return "I do not have an age."
    else:
        return "I am not yet configured to understand that..."
    #main program
def chatbot():
    #welcome statement
    print("Hi! My name is chatrtm, your first ever chatbot(type exit to quit)")
    while True:
        user_input=input("You:")
        if "exit" in user_input:
            break
        #get the response
        ai_response=response(user_input)
        print("Chatrtm:",ai_response)
#run the program
if __name__=="__main__":
    chatbot()