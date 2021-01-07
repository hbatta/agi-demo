from PlacementPortal.forms import GetStudentDetails
from django.shortcuts import render
from django.views import View
from PlacementPortal.models import *
from django.http import HttpResponse
import pandas as pd
from io import BytesIO as IO


class QueryDb(View):

    def get(self, request):
        print("abcd")
        form = GetStudentDetails()
        return render(request, "PlacementPortal/query_form.html", context={'form': form})

    def post(self, request, *args, **kwargs):
        form = GetStudentDetails(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            gender = data['gender']
            tenth = data['tenth']
            inter = data['inter']
            btech = data['btech']
            backlogs = data['backlogs']
            caste = data['caste']
            department = data['department']

            index = 0
            for i in gender:
                if i == '0':
                    gender = [True, False]
                    break
                elif i == 'Male':
                    gender[index] = True
                elif i == 'Female':
                    gender[index] = False
                index = index + 1

            for i in department:
                if i == '0':
                    department = ['CSE', 'ECE', 'CIVIL', 'MECH', 'IT', 'CHEM']
                    break

            for i in caste:
                if i == '0':
                    caste = ['OC', 'SC', 'ST', 'BC']
                    break

            data_res = Student.objects.values("pk", "first_name", "last_name", "hall_ticket_number", "gender",
                                              'date_of_birth',
                                              "backlogs", "caste", "tenth_marks", "department__acronym",
                                              "inter_marks", "btech_marks").order_by("pk").filter(
                inter_marks__gte=inter, btech_marks__gte=btech, tenth_marks__gte=tenth,
                backlogs__lte=backlogs, gender__in=gender,
                department__acronym__in=department)

            res_arr = []
            res_arr.append(
                ['Name', 'Hall Ticket Number', 'Department', 'DOB', 'Gender', 'Caste', 'Tenth %', 'Inter %', 'Btech %',
                 'Backlogs'])

            index = 0
            for item in data_res:
                name = data_res[index]['first_name'] + data_res[index]['last_name']
                hallticket = data_res[index]['hall_ticket_number']
                dept = data_res[index]['department__acronym']
                dob = str(data_res[index]['date_of_birth'])
                gender = None
                if data_res[index]['gender']:
                    self.gender = 'Male'
                else:
                    self.gender = 'Female'

                caste = data_res[index]['caste']
                tenth = data_res[index]['tenth_marks']
                inter = data_res[index]['inter_marks']
                btech = data_res[index]['btech_marks']
                backlogs = data_res[index]['backlogs']

                res_arr.append([name, hallticket, dept, dob, self.gender, caste, tenth, inter, btech, backlogs])
                index = index + 1
            df_output = pd.DataFrame(res_arr)
            excel_file = IO()

            xlwriter = pd.ExcelWriter(excel_file, engine='xlsxwriter')
            df_output.to_excel(xlwriter, 'sheetname')

            xlwriter.save()
            xlwriter.close()
            excel_file.seek(0)
            response = HttpResponse(excel_file.read(),
                                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=myfile.xlsx'

            return response
