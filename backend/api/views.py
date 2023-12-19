from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Payment
from .serializers import UserSerializer

def validate_age(age):
    return age >= 18 and age <= 65

# returns the payment object if payment is successful, None otherwise
# for this application, we assume that payment is always successful, hence, we always return the payment object  
def CompletePayment(payment_details):
    payment_object = Payment.objects.create(details = payment_details)
    return payment_object

class DataValidation(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = {
            'user_name': request.data.get('name'),
            'user_email': request.data.get('email'),
            'user_age': request.data.get('age'),
            'user_batch': request.data.get('batch'),
            'payment_details': request.data.get('paymentDetails'),
        })   
        
        # if the request data is not valid
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user_name = serializer.validated_data['user_name']
        user_email = serializer.validated_data['user_email']
        user_age = serializer.validated_data['user_age']
        user_batch = serializer.validated_data['user_batch']
        payment_details = serializer.validated_data['payment_details']

        # if the age is not valid
        if not validate_age(user_age): 
            return Response({"message": "Age must be between 18 and 65."}, status=status.HTTP_400_BAD_REQUEST)
        
        payment = CompletePayment(payment_details)

        if(payment == None):
            return Response({"message": "Payment details not valid"}, status=status.HTTP_400_BAD_REQUEST)
        
        User.objects.create(name = user_name, email = user_email, age = user_age, batch = user_batch, payment = payment)
        
        return Response({"message": f"Payment successful\n Payment id: {payment.id}"}, status=status.HTTP_200_OK)




            