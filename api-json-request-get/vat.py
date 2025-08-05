import json

tekst_json = '''{
  "currency": "PLN",
  "vat_rate": 0.23,
  "items": [
    { "name": "Notes A5", "qty": 2, "unit_price": 7.50 },
    { "name": "Długopis", "qty": 3, "unit_price": 2.20 },
    { "name": "Marker", "qty": 1, "unit_price": 5.90 }
  ]
}'''
data = json.loads(tekst_json)  # zamiana na słownik Pythona

suma = 0
for item in data['items']:
    netto = round(item["unit_price"] * item["qty"],2)
    print(item["name"], "x", item["qty"], " = ", netto, data["currency"])
    suma += netto

print("-----------------------")
print(f"Suma netto: {suma} PLN")

vat = round(suma * data["vat_rate"],2)
print (f"VAT 23%: {vat} PLN")
print((f"Suma brutto: {suma + vat} PLN"))




