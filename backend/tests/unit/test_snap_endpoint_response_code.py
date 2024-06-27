from application.models.snap import Snap
from sqlalchemy.sql.expression import func

def test_snaps_list_endpoint_response_code(test_client, init_database):
    random_snap = Snap.query.order_by(func.random()).first()
    response = test_client.get(f'/api/v1/snaps/{random_snap.unique_code}')
    assert response.status_code == 200
