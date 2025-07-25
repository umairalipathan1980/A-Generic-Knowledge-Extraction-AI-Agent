# Auto-generated Pydantic models
# Generated by Knowledge Extraction Agent

```python
from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class CarType(str, Enum):
    SEDAN = "sedan"
    HATCHBACK = "hatchback"
    COUPE = "Coupe"
    CONVERTIBLE = "Convertible (Cabriolet)"
    SUV = "SUV (Sport Utility Vehicle)"
    CROSSOVER = "Crossover (CUV)"
    STATION_WAGON = "Station Wagon (Estate)"
    PICKUP_TRUCK = "Pickup Truck"

class InvoiceInfo(BaseModel):
    name: str = Field(..., description="name of the recepient")
    address: str = Field(..., description="recepient's address")
    amount: str = Field(..., description="invoice amount")
    due_date: str = Field(..., description="the date on which the invoice is due.")
    bank_name: str = Field(..., description="Name of the bank")
    car_type: CarType = Field(..., description="type of the car")
```