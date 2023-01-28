from xia_fields import StringField
from xia_fields_network import EmailField
from xia_engine import Document
from xia_engine import ExternalField


class Customer(Document):
    id: str = EmailField(description="Customer Email")
    name: str = StringField(description="Customer Name")


class PurchaseOrder(Document):
    po_number: str = StringField(description="Purchase Order Number")
    order_status: str = StringField(description="Purchase Order Status",
                                    required=True,
                                    default="new",
                                    choices=["new", "paid", "delivered"])
    customer: str = StringField(description="Customer")
    customer_detail = ExternalField(document_type=Customer,
                                    description="Customer Detail",
                                    field_map={"customer": "id"})
