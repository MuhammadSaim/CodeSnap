from application.models.snap import Snap
from sqlalchemy.sql.expression import func

# test to get the response from a snap image, images are served successfully
def test_snap_image_response(test_client, init_database):
    random_snap = Snap.query.order_by(func.random()).first()
    response = test_client.get(f'/images/snap/{random_snap.unique_code}')
    assert response.status_code == 200
