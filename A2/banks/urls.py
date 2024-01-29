from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name= 'bankform' ),
    path('bankform/', views.BankView.as_view(), name= 'bankform' ),
    path('branchform/', views.BranchView.as_view(), name= 'branchform' ),
    path('bankupdate/<int:pk>/', views.BankUpdateView.as_view(), name='bankupdate'),
    path('branchupdate/<int:pk>/', views.BranchUpdateView.as_view(), name='branchupdate'),
    path('bankdelete/<int:pk>/', views.BankDeleteView.as_view(), name="bankdelete"),
    path('branchdelete/<int:pk>/', views.BranchDeleteView.as_view(), name="branchdelete"),

    # path('bankform/', views.BankView.as_view(), name= 'bankform' ),
]


