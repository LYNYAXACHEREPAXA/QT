# відкриваємо файл 'quotes.txt' для читання
with open("quotes.txt","r",encoding = "UTF-8") as file:
    for line in file:
        print(line)

answer = input('Хто написав ці рядки?')

# відкриваємо файл 'quotes.txt' для додавання даних
with open("quotes.txt","a",encoding = "UTF-8") as file:
    file.write("\n", answer)



while True:
    answer = input("Бажаєте додати ще одну цитату? так/ні:   ")
    answer = answer.lower()
    if answer == "так":
        quote = input('Введіть цитату  ')
        author = input('Введіть автора  ')
        with open("quotes.txt","a",encoding = "UTF-8") as file:
            file.write("\n", author)
            file.write("\n", quote)
            file.close()
    else:
        break

with open("quotes.txt","r",encoding = "UTF-8") as file:
    for line in file:
        print(line)

