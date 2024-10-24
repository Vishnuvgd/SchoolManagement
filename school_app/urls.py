from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('adminreg/',Adminreg,name='adminreg'),
    path('adminlog/',Adminlog,name='adminlog'),
    path('adminlogfail/',Adminlogfail,name='adminlogfail'),
    
    path('studentform/',student_form, name='studentform'),
    path('studentslist/',student_list, name='studentlist'),
    path('studentsview/',student_view, name='studentview'),
    path('studentdel/<int:id>',student_del,name='studentdel'),
    path('studentedit/<int:id>',student_edit,name='studentedit'),
    
    path('officereg/',Office_reg,name='officereg'),  
    path('officelog/',Office_log,name='officelog'),  
    path('officeview/',office_view,name='officeview'),
    path('officeprofile/',office_profile,name='officeprofile'),
    
    path('officeform/',staff_form,name='officeform'),
    path('officelist/',office_list,name='officelist'),
   
    path('staffdel/<int:id>',staff_del,name='staffdel'),
    path('staffedit/<int:id>',staff_edit,name='staffedit'),
      
    path('libraryreg/',library_reg,name='libraryreg'),  
    path('librarylog/',library_log,name='librarylog'),  
    path('libraryview/',library_view,name='libraryview'),
    path('librarylist/',library_list,name='librarylist'),
    path('librarydel/<int:id>',library_del,name='librarydel'),
    path('booklist/',Book_list,name='booklist'),
      
    path('feeview/',fee_view,name='feeview'),  
    path('feelist/',fee_list,name='feelist'),  
]
