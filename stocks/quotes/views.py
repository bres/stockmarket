from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import StockForm
from .models import Stock


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
def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form =StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("stock has been added"))
            return redirect('add_stock')

    else:
        ticker=Stock.objects.all()
        output=[]
        for ticker_item in ticker:
            api_request = requests.get(
                "https://sandbox.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=Tpk_a5a08a1f80354252a30520ef83683ecb")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "error"
        return render(request,'add_stock.html',{'ticker':ticker,'output':output})

def delete(request, stock_id):
        item =Stock.objects.get(pk=stock_id)
        item.delete()
        messages.success(request,("Stock has been deleted"))
        return redirect('delete_stock')


def delete_stock(request):
    ticker = Stock.objects.all()

    return render(request,'delete_stock.html',{'ticker':ticker })


