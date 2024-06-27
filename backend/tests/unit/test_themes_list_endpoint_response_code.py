def test_themes_list_endpoint_response_code(test_client, init_database):
    response = test_client.get('/api/v1/themes')
    print(response.headers)
    assert response.status_code == 200
    