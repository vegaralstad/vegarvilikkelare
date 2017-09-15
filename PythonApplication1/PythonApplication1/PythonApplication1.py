import webbrowser

url1 = ""
url2 = ""

print ("Are you good bro?")


var = input("Yes/no: ")
if var == "yes":

    try:
        webbrowser.open(url1, 2, False);
    except Exception as e:
        raise


if var == "no":

    try:
        webbrowser.open(url2, 2, False);
    except Exception as e:
        raise


print ("Thank you for your respons"), var,
