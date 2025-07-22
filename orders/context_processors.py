from forms import QuickOrderForm

def quick_order_form(request):
    return {'quick_order_form': QuickOrderForm()}