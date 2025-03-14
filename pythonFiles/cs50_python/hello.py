import numpy as np
from scipy.optimize import curve_fit

# Resistance and temperature data
resistance = np.array([32407.13, 31598.11, 30811.658, 30047.084, 29303.72, 28580.92, 27878.061, 27194.537, 26529.766, 25883.182, 
                       25254.239, 24642.409, 24047.178, 23468.054, 22904.556, 22356.222, 21822.603, 21303.264, 20797.785, 20305.76, 
                       19826.795, 19360.507, 18906.529, 18464.501, 18034.079, 17614.926, 17206.718, 16809.139, 16421.886, 16044.662, 
                       15677.181, 15319.166, 14970.348, 14630.467, 14299.271, 13976.514, 13661.959, 13355.376, 13056.544, 12765.244, 
                       12481.268, 12204.413, 11934.481, 11671.281, 11414.629, 11164.342, 10920.249, 10682.178, 10449.967, 10223.455, 
                       10002.488, 9786.9153, 9576.5921, 9371.3768, 9171.1321, 8975.7248, 8785.0256, 8598.909, 8417.2531, 8239.9396, 8066.8535,
                       7897.8832, 7732.9204, 7571.8597, 7414.5989, 7261.0386, 7111.0825, 6964.6366, 6821.61, 6681.9141, 6545.4628, 6412.1727,
                       6281.9625, 6154.7532, 6030.4682, 5909.0327, 5790.3743, 5674.4226, 5561.1088, 5450.3665, 5342.1308, 5236.3387, 5132.9289,
                       5031.8417, 4933.0193, 4836.4053, 4741.9447, 4649.5842, 4559.2719, 4470.9573, 4384.5912, 4300.1259, 4217.5147, 4136.7125,
                       4057.675, 3980.3594, 3904.724, 3830.7281, 3758.332, 3687.4974, 3618.1867, 3550.3633, 3483.9917, 3419.0373, 3355.4663,
                       3293.2459, 3232.3441, 3172.7297, 3114.3725, 3057.2427, 3001.3117, 2946.5514, 2892.9344, 2840.434, 2789.0244, 2738.6802,
                       2689.3767, 2641.0901, 2593.7967, 2547.4738, 2502.0992])

temperature_C = np.arange(0, 60.5, 0.5)  # Temperature in Celsius

# Convert temperature to Kelvin
temperature_K = temperature_C + 273.15

# Define the Steinhart-Hart equation
def steinhart_hart_equation(R, T0, B):
    return 1 / (1/T0 + 1/B * np.log(R))

# Fit the Steinhart-Hart equation to the data
popt, pcov = curve_fit(steinhart_hart_equation, resistance, 1/temperature_K, bounds=([0, 0], [np.inf, np.inf]), p0=[273.15, 3000])  

# Provide initial guess for T0 and B and set bounds

# Extract the Beta coefficient (B)
B = popt[1]
print("Beta coefficient (B):", B)
