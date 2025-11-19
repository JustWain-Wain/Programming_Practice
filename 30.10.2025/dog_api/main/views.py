import requests
from django.shortcuts import render

breeds_list = [i for i in requests.get("https://dog.ceo/api/breeds/list/all").json()["message"]]


def dog_image_view(request):
    # Получаем список пород

    breed = request.GET.get('breed', '').strip().lower()
    image_url = None
    error = None

    if breed:
        api_url = f"https://dog.ceo/api/breed/{breed}/images/random"
        try:
            response = requests.get(api_url)
            data = response.json()

            if data['status'] == 'success':
                image_url = data['message']
            else:
                error = "Порода не найдена или ошибка в API."
        except Exception as e:
            error = f"Ошибка при запросе к API: {e}"

    context = {
        'breed': breed,
        'image_url': image_url,
        'error': error,
        'breeds_list': breeds_list,  # передаём список пород в шаблон
    }

    return render(request, 'main/page.html', context)