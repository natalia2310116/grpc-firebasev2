from firebase.conexion import conexion
from grpc.grpc_server import serve
from services.product_service import get_all_product


def init():
    conexion()
    get_all_product()
    serve()


if __name__=="__main__":
    init()
