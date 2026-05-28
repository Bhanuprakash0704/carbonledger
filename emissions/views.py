from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import Tenant, Source, EmissionRecord
from .serializers import EmissionRecordSerializer

from ingestion.sap_parser import parse_sap_csv


class SAPUploadView(APIView):

    def post(self, request):

        try:

            print("========== REQUEST RECEIVED ==========")

            print("FILES:", request.FILES)

            file = request.FILES.get('file')

            if not file:
                return Response({
                    "error": "No file uploaded"
                }, status=400)

            print("File received:", file.name)

            tenant = Tenant.objects.first()

            print("Tenant:", tenant)

            if not tenant:
                return Response({
                    "error": "No tenant found"
                }, status=400)

            source = Source.objects.create(
                tenant=tenant,
                source_type='sap',
                file_name=file.name
            )

            print("Source created")

            parsed_records = parse_sap_csv(file)

            print("Parsed Records:", parsed_records)

            for item in parsed_records:

                print("Creating record:", item)

                EmissionRecord.objects.create(
                    tenant=tenant,
                    source=source,
                    category=item['category'],
                    scope=item['scope'],
                    quantity=item['quantity'],
                    unit=item['unit'],
                    normalized_quantity=item['normalized_quantity'],
                    normalized_unit=item['normalized_unit'],
                    co2e=item['co2e'],
                    suspicious=item['suspicious']
                )

            print("All records inserted successfully")

            return Response({
                "message": "SAP CSV uploaded successfully"
            })

        except Exception as e:

            print("ERROR:", str(e))

            return Response({
                "error": str(e)
            }, status=500)
class EmissionRecordListView(ListAPIView):

    queryset = EmissionRecord.objects.all().order_by('-created_at')

    serializer_class = EmissionRecordSerializer




# from rest_framework.views import APIView
# from rest_framework.response import Response

# from .models import Tenant, Source, EmissionRecord
# from ingestion.sap_parser import parse_sap_csv


# class SAPUploadView(APIView):

#     def post(self, request):

#         try:

#             print("========== REQUEST RECEIVED ==========")

#             print("FILES:", request.FILES)

#             file = request.FILES.get('file')

#             if not file:
#                 return Response({
#                     "error": "No file uploaded"
#                 }, status=400)

#             print("File received:", file.name)

#             tenant = Tenant.objects.first()

#             print("Tenant:", tenant)

#             if not tenant:
#                 return Response({
#                     "error": "No tenant found"
#                 }, status=400)

#             source = Source.objects.create(
#                 tenant=tenant,
#                 source_type='sap',
#                 file_name=file.name
#             )

#             print("Source created")

#             parsed_records = parse_sap_csv(file)

#             print("Parsed Records:", parsed_records)

#             for item in parsed_records:

#                 print("Creating record:", item)

#                 EmissionRecord.objects.create(
#                     tenant=tenant,
#                     source=source,
#                     category=item['category'],
#                     scope=item['scope'],
#                     quantity=item['quantity'],
#                     unit=item['unit'],
#                     normalized_quantity=item['normalized_quantity'],
#                     normalized_unit=item['normalized_unit'],
#                     co2e=item['co2e'],
#                     suspicious=item['suspicious']
#                 )

#             print("All records inserted successfully")

#             return Response({
#                 "message": "SAP CSV uploaded successfully"
#             })

#         except Exception as e:

#             print("ERROR:", str(e))

#             return Response({
#                 "error": str(e)
#             }, status=500)