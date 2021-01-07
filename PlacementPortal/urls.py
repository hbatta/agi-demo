from django.urls import path
from .views import *
from .api import *

app_name = "PlacementPortal"

urlpatterns = [

    path('login/', LoginUser.as_view(), name="login_url"),
    path('logout/', logout_user, name="logout"),

    path('department/<int:dept_id>/student/<int:pk>/marks/', MarkList.as_view(), name="student_marks"),
    path('department/<int:dept_id>/student/<int:pk>/contact/', ContactDetail.as_view(), name="student_contact"),

    path('department/', DepartmentList.as_view(), name="department_list"),
    path('department/<int:dept_id>/student/', DepartmentStudentList.as_view(), name="department_student_list"),
    path('department/<int:dept_id>/student/<int:pk>/edit', DepartmentStudentEdit.as_view(),
         name="department_student_edit"),
    path('department/<int:pk>/delete/', DepartmentDelete.as_view(), name="department_delete"),
    path('department/<int:pk>/edit/', DepartmentUpdate.as_view(), name="department_update"),
    path('department/add/', DepartmentCreate.as_view(), name="department_add"),

    path('home/', Home.as_view(), name="home"),
    path('', LoginUser.as_view(), name="login"),

    path('studentUpload/', studentUpload, name="student_file_upload"),
    path('marksUpload/', marksUpload, name="marks_file_upload"),
    path('query/', QueryDb.as_view(), name='select_query'),



    # api urls
    path('api/', StudentListView.as_view(), name="api_student_list"),
    path('api/<str:htno>/', StudentDetailView.as_view(), name="api_student_detail"),
]


