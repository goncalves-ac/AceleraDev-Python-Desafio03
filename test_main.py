from main import get_temperature
from unittest.mock import patch
import pytest 


@pytest.mark.parametrize('temp_dada, lat, lng, result_esperada',[(62, -14.235004, -51.92528, 16),(17, 15.356987, -45.152367, -8),(-189, 25.012809, -25.012809, -122),(100, 0, 0, 37)])
def test_get_temperature_by_lat_lng(temp_dada, lat, lng, result_esperada):

    mock_get_patcher = patch('main.requests.get') #pega a patch do main que esta no request 'linha 7'

    temperature = { #criou-se o objeto baseado no que eu quero
        'currently':{
            'temperature': temp_dada
        }
    }

    mock_get = mock_get_patcher.start() #inicia o mock

    mock_get.return_value.json.return_value = temperature # faz a chamada em IPA eu coloca a temperatura que eu quero

    response_value_chamada = get_temperature(lat, lng) #chamar a função na resposta que eu quero

    mock_get_patcher.stop() #parar de colocar o objeto nas requissições.

    assert response_value_chamada == result_esperada
