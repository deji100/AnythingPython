import telnyx

telnyx.api_key = "KEY0185F3DFB6FF8BA37377156B52E04A3C_FWXTWIHjRBjZaNUOtiby0U"

telnyx.NumberOrder.create(
  phone_numbers=[{"phone_number": "+18722165438"}]
)