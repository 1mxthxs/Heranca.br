from django.shortcuts import redirect

class CustomErrorHandler:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            return redirect('error')  # Redireciona para a página de erro
        return response
