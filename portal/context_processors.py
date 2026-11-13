from .models import Menu

def menu_dinamico(request):
    itens_menu = Menu.objects.filter(ativo=True).order_by('ordem')
    return {'menu_itens': itens_menu}
