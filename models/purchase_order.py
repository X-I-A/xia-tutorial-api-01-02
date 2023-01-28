from xia_fields import StringField
from xia_fields_network import EmailField
from xia_engine import Document, EmbeddedDocument
from xia_engine import ExternalField, EmbeddedDocumentField


class Customer(Document):
    id: str = EmailField(description="Customer Email")
    name: str = StringField(description="Customer Name")


class DeliveryAddress(EmbeddedDocument):
    address: str = StringField(description="Delivery Address")


class PurchaseOrder(Document):
    po_number: str = StringField(description="Purchase Order Number")
    order_status: str = StringField(description="Purchase Order Status",
                                    required=True,
                                    default="new",
                                    choices=["new", "paid", "delivered"])
    delivery_address = EmbeddedDocumentField(document_type=DeliveryAddress)
    customer: str = StringField(description="Customer")
    customer_detail = ExternalField(document_type=Customer,
                                    description="Customer Detail",
                                    field_map={"customer": "name"})
