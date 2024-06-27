from pygments.styles import get_all_styles

def test_themes_list_endpoint_response_code(test_client, init_database):
    response = test_client.get('/api/v1/themes')
    response_data = response.get_json()
    themes = list(get_all_styles())
    assert len(response_data) == len(themes) 
    assert response.status_code == 200
    