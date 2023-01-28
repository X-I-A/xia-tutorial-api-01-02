# X-I-A API Tutorial - 01-02: Advanced Data Model
## Getting Started

Welcome to XIA API tutorial!

The goal of this tutorial is to quickly show you how to build a complex application by using X-I-A API framework. 
This framework is microservice based in order to get a fast learning curve for developers and AI.

## How to use this tutorial

Each tutorial is ended by a series number like 01-02-03. The longer the series is, the more advanced topic is discussed.
It will be better to finish basic tutorial before going through advanced ones. Each tutorial has example code. 
Installation instruction could be found at tutorial/install.md.

## Prerequisites

Already finish the reading of
* [Tutorial API 01](https://github.com/X-I-A/xia-tutorial-api-01)
* [Tutorial API 01-01](https://github.com/X-I-A/xia-tutorial-api-01-01)

## Start with example

Please clone and deployed the example code (see [installation guide](tutorial/install.md) for instruction).

Or just visiting the already deployed [online version](https://xia-tutorial-api-01-02-srspyyjtqa-ew.a.run.app/order)

Here is a 40-second-video to show briefly how the new data model impacts the editor and api endpoints:

https://user-images.githubusercontent.com/49595269/215292487-7e7bf274-4a0b-4cab-9747-d36b2b9e866b.mp4


## Complex data model
### Relationship

The last part of [Tutorial API 01-01](https://github.com/X-I-A/xia-tutorial-api-01-01) explained that the embedded 
document represents the information which should be a part of the document. The other case of relationship between two 
data models is the simple link. In the given example code, a purchase order holds the customer id and from the id we
could retrieve the customer's full information.

This link could be defined easily with adding an ExternalField into data model `PurchaseOrder`:
```
    customer_detail = ExternalField(document_type=Customer,
                                    description="Customer Detail",
                                    field_map={"customer": "id"})
```
* `document_type` defines the related data model is `Customer`
* `field_map` defines the field mapping: `PurchaseOrder`.`customer` = `Customer`.`id`

It is possible to add multiple field map. The result could also be a list. Check [technical document]((https://develop.x-i-a.com/docs/xia-engine/stable/_autosummary/xia_engine.fields.ExternalField.html#xia_engine.fields.ExternalField)) for more details.

### Modifications:

Here are the modifications we have made to Tutorial 01. 

* models/purchase_order.py:
    * Adding Customer data model
    * Adding dependency of email field (also need to add dependency in `requirements-xia.txt`)
* config.py
    * Adding new mapping `"customer": Customer` to `RESOURCE_MAPPING`

Yes, that is all

### Lazy Load

To avoid over-fetching data, the default retrieve mode is lazy:
* All external field won't be loaded from related data model
* All runtime data won't be unpacked. For an example, if a field is stored compressed, only compressed data will be 
shown in default mode.

To make the model load all data, we must add `lazy=false` parameter.

The default behavior will help to render the frontend part by part. We have also using catalog parameter to avoid 
under-fetching. More detail will be given at 
* Tutorial 01-03: Framework natively avoids over fetching and under fetching
