from django.shortcuts import render

# Create your views here.
#pk_14bef050968e4bd98eed52c4072a05cd

def home(request):
    import requests
    import json
    if request.method == 'POST':
        ticker=request.POST['ticker']
        api_request = requests.get("https://sandbox.iexapis.com/stable/stock/" + ticker + "/quote?token=Tpk_a5a08a1f80354252a30520ef83683ecb")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error"
        return render(request, 'home.html', {'api':api})

    else:
        return render(request,'home.html',{'ticker':"bla bla bla"})



def about(request):
    return render(request,'about.html',{})