import pytest

@pytest.fixture
def create_admin_user(django_user_model):
  """
  Retorna el usuario administrador
  """
  
  return django_user_model.objects.create_superuser("admin", "a@a.com", "password")
  