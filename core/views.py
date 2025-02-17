# pdfgen/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os

os.add_dll_directory(r"C:\Users\windo\Downloads\GTK-for-Windows-Runtime-Environment-Installer-2022-01-04\gtk-nsis-pack\bin")
from weasyprint import HTML
from django.http import HttpResponse

# pdfgen/serializers.py
from rest_framework import serializers

class PdfGenerationSerializer(serializers.Serializer):
    text = serializers.CharField()


class GeneratePdfView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PdfGenerationSerializer(data=request.data)
        
        if serializer.is_valid():
            text = serializer.validated_data['text']
            html_content = f"<html><body><h1>{text}</h1></body></html>"
            
            # Generate PDF from HTML content
            pdf_file = HTML(string=html_content).write_pdf()
            
            # Return the PDF as an HTTP response
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="generated.pdf"'
            return response
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
