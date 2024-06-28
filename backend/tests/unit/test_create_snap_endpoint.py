from application.models.language import Language
from application.models.theme import Theme
from sqlalchemy.sql.expression import func
from application.helpers.general_helpers import (
    generate_fake_image,
    pil_image_to_base64
)
from random import randrange

# initiate the test to create snap end point
def test_create_snap_endpoint(test_client, init_database):
    theme = Theme.query.order_by(func.random()).first()
    language = Language.query.order_by(func.random()).first()
    base_64_image = pil_image_to_base64(generate_fake_image(
        randrange(
            randrange(800, 1200),
            randrange(1200, 2000),
        ),
        randrange(
            randrange(200, 400),
            randrange(800, 1200),
        )
    ))
    response = test_client.post('/api/v1/snaps', json={
        'snap': base_64_image,
        'language_id': language.id,
        'theme_id': theme.id
    })
    
    response_data = response.get_json()
    
    assert response.status_code == 201
    
    assert response_data['message'] == 'Snap created successfully'
    
    assert response_data['data']['theme'] == theme.name
    