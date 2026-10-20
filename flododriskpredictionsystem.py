# Coding — Python
# AI-Based Flood Risk Prediction System

rainfall = float(input("Enter rainfall (mm): "))
water_level = float(input("Enter water level (m): "))
temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))

score = 0

if rainfall > 100:
    score += 40
elif rainfall > 50:
    score += 20

if water_level > 5:
    score += 40
elif water_level > 3:
    score += 20

if humidity > 80:
    score += 10

if temperature > 30:
    score += 10

if score >= 70:
    risk = "HIGH"
elif score >= 40:
    risk = "MEDIUM"
else:
    risk = "LOW"

print("\n--- Flood Risk Prediction ---")
print("Flood Risk Score:", score, "%")
print("Risk Level:", risk)


