from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import google.generativeai as genai
import os

# genai.configure(api_key=os.environ["API_KEY"])
genai.configure(api_key="AIzaSyDW53fxktsx34AlYU3We5yrVcn-vHRQ6T4")


@api_view(['POST'])
def process_data(request):
    data = request.data
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Advice the user on how to improve their device usage. in  50 words", **data)
    print(response.text)
    
    # Process the data (replace this with your actual processing logic)
    processed_result = response.text

    if processed_result:
        return Response({
            "status": "success",
            "result": processed_result
        })

    return Response({
        "status": "error",
        "message": "No data to process"
    }, status=status.HTTP_400_BAD_REQUEST)
