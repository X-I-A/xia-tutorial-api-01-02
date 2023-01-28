from models.purchase_order import PurchaseOrder, Customer


class Config:
    DEBUG = True
    DEVELOPMENT = True
    APP_NAME = 'xia-tutorial-api-01-02'
    APP_DESCRIPTION = "X-I-A Tutorial API - 01 - 02 - Complex Data Model"
    RESOURCE_MAPPING = {
        "order": PurchaseOrder,
        "customer": Customer
    }


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProdConfig(Config):
    DEBUG = True
    DEVELOPMENT = False
