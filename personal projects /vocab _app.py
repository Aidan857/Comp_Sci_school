import random


vocab = {
    "pen" : "boligrafo",
    "pencilsharpener" : "afilagrfo",
    "pencil" : "lápiz",
    "table" : "mesa",
    "chair" : "sila",
    "student" :"alumno",
    "bag" :"mochila",
    "clock" : "reloj",
    "chalk" : "tiza", 
    "draw" : "dibujar"

}

#make the terminal ask questions and then add a library and make it graphical 

#shuffle the words randomly 
words = list(vocab.keys())
random.shuffle(words)

correct = 0
attempts =0
# print each word one by one 
print("give me the answer in spanish")
for key in words:
    user = input(f"{key}: ")

    if user == vocab[key]:
        correct += 1
        print(f"correct: {correct}")
    
    else:
        print ("incorrect")
        user = input(f"{key}: ")
        attempts += 1

        

       

    attempts += 1
    print(f"attempts:{attempts}")



    
        
 
