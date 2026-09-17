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

WEIGHT_TO_G = {
    WeightUnit.GRAM: Decimal('1'),
    WeightUnit.KILOGRAM: Decimal('1000'),
    WeightUnit.OUNCE: Decimal('28.3495'),
    WeightUnit.POUND: Decimal('453.592'),
}

def convert_weight(value, from_unit, to_unit):
    value = Decimal(value)
    value_in_g = value * WEIGHT_TO_G[from_unit]
    return value_in_g / WEIGHT_TO_G[to_unit]

