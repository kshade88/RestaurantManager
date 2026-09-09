from decimal import Decimal
from .choices import VolumeUnit, WeightUnit

VOLUME_TO_ML = {
    VolumeUnit.MILLILITER: Decimal('1'),
    VolumeUnit.LITER: Decimal('1000'),
    VolumeUnit.FLUID_OUNCE: Decimal('29.5735'),
}

def convert_volume(value, from_unit, to_unit):
    value = Decimal(value)

    value_in_ml = value * VOLUME_TO_ML[from_unit]
    return value_in_ml / VOLUME_TO_ML[to_unit]

