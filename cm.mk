## Specify phone tech before including full_phone
$(call inherit-product, vendor/cm/config/gsm.mk)

# Release name
PRODUCT_RELEASE_NAME := amazingtrfcd

# Inherit some common CM stuff.
$(call inherit-product, vendor/cm/config/common_full_phone.mk)

# Inherit device configuration
$(call inherit-product, device/samsung/amazingtrfcd/device_amazingtrfcd.mk)

## Device identifier. This must come after all inclusions
PRODUCT_DEVICE := amazingtrfcd
PRODUCT_NAME := cm_amazingtrfcd
PRODUCT_BRAND := samsung
PRODUCT_MODEL := amazingtrfcd
PRODUCT_MANUFACTURER := samsung
