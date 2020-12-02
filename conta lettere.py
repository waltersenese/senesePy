print("questo programma conta quante volte la a è all'interno di una parola ")
domanda = input("\nvuoi cominciare (si\no) ")

if(domanda == "no" or domanda == "No"):
   print ("Ok, grazie del tuo tempo alla prossima ")
   exit
elif(domanda == "si" or domanda == "Si"):
   print("Ok, allora scrivi una parola")
else:
  print("Scusa non ho capito")
  exit
  
a = input()
conta = 0

for x in a:
  if x =="a":

    conta=conta+1
print(conta)

