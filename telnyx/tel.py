import telnyx

telnyx.api_key = ""

telnyx.NumberOrder.create(
  phone_numbers=[{"phone_number": "+18722165438"}]
)
