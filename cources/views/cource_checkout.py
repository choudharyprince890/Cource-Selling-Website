from django.http import HttpResponse
from django.shortcuts import redirect, render
from cources.models.cource import *
from cources.models.videos import Videos
from cources.models.payment import Payment
from cources.models.user_cource import UserCource
import razorpay
from django.views.decorators.csrf import csrf_exempt 
from gdemy.settings import KEY_SECRET, KEY_ID
client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
from time import time

def checkout(request, slug):
    # print(request.user)
    cource = Cource.objects.get(slug=slug)
    user = None
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    action = request.GET.get('action')
    order = None
    error_msg = None
    if action == 'create_payment':
        try:
            user_cource = UserCource.objects.get(user=user,cource=cource)
            error_msg = "You are Already Enrolled in this Course" 
        except:
            pass
        if error_msg is None:
            data = {
            'amount' : (cource.prince)*100,
            'currency' : 'INR',
            # 'reciept' : f'gdemy-{int(time())}',
            'notes' : {
                'email': user.email,
                'name': f'{user.first_name} {user.last_name}',
            },
            }
            order = client.order.create(data=data)
            payment = Payment()
            payment.user = user
            payment.cource = cource
            payment.order_id = order.get('id')
            payment.save()

        print('creating order object')
    data = {'cources':cource,
            'order':order,
            'error_msg': error_msg
            }
    return render(request, 'cources/checkout.html', data)


@csrf_exempt    
def verifyPayment(request):
    if request.method == 'POST':
        data = request.POST
        print('this is dataaa//.,..')
        print(data)
        razor_id = data.get('razorpay_order_id')
        razor_payment_id = data.get('razorpay_payment_id')
        razor_signature = data.get('razorpay_signature')
        params_dict = {
            'razorpay_order_id': razor_id,
            'razorpay_payment_id': razor_payment_id,
            'razorpay_signature': razor_signature
        }


# updating the payment model with payment.id and status 
        payment = Payment.objects.get(order_id=razor_id)
        payment.payment_id = razor_payment_id
        payment.status = True
        payment.save()


#  creating usercource in model 
        user_cource = UserCource()
        user_cource.user = payment.user
        user_cource.cource = payment.cource
        user_cource.save() 

# updating the payment model with payment.id and status 
        payment.user_cource = user_cource
        payment.save()




        context = {
            'data': params_dict
        }
        print('this is dict...',params_dict)
        try:
            return render(request, 'cources/my_cources.html', context)
            # client.utility.verify_payment_signature(params_dict)
        except:
            return HttpResponse('invalid payment')

