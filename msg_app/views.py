from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import Body, Media, Message, MessagingResponse


@csrf_exempt 
def sms_reply(request):
    print(request.POST)
    msg = request.POST['Body']
    sender = request.POST['From'].split(':')
    resp = MessagingResponse()
    message = Message()
    print(msg)
    message.body(f'Hello. *You said:* {msg}')
    message.media('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=1200:*')
    resp.append(message)
    return HttpResponse(resp)
