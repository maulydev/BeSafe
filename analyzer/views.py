from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def process_data(request):
    data = request.data
    # Process the data (replace this with your actual processing logic)
    processed_result = "Your device usage for the day is 10 hours and compared to the average usage of 8 hours, you are 2 hours over the limit."

    if processed_result:
        return Response({
            "status": "success",
            "result": processed_result
        })

    return Response({
        "status": "error",
        "message": "No data to process"
    }, status=status.HTTP_400_BAD_REQUEST)
