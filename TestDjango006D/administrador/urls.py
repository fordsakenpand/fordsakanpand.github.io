from .views import login

urlpatterns = [
    path ('login.html',login,name="login")
]