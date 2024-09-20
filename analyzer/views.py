from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
import os
from health_profile.models import Profile
from advice.models import Advice


# genai.configure(api_key=os.environ["API_KEY"])
genai.configure(api_key="AIzaSyDW53fxktsx34AlYU3We5yrVcn-vHRQ6T4")


@api_view(['POST'])
def process_data(request):
    data = request.data

    # get user profile data
    user_profile = Profile.objects.filter(
        user__username=data.get('username')).first()

    # create dictionary of the profile data
    data = {
        "age": user_profile.age if user_profile else None,
        "occupation": user_profile.occupation if user_profile else None,
        "avg_screen_time": user_profile.avg_screen_time if user_profile else None,
        "health_response": user_profile.health_response if user_profile else None,
        "screen_time_today": data.get('screen_time_today')
    }

    ai_clue = "Analyze this user information and provide a very short advice on how to improve device usage, just use the data.\n"

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{ai_clue} {data}")
    print(response.text)

    # Process the data (replace this with your actual processing logic)
    processed_result = response.text
    
    if user_profile: Advice.objects.create(profile=user_profile, content=processed_result)
    

    if processed_result:
        return Response({
            "status": "success",
            "result": processed_result
            # "result": data
        })

    return Response({
        "status": "error",
        "message": "No data to process"
    }, status=status.HTTP_400_BAD_REQUEST)
