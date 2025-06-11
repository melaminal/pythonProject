import os

# Initialize list to store results
results = []

# Walk through all subdirectories in the current directory
for dirname in os.listdir(".."):
    if os.path.isdir(dirname):
        outcar_path = os.path.join(dirname, "OUTCAR")
        if os.path.isfile(outcar_path):
            try:
                # Open the OUTCAR file and read lines
                lines = open(outcar_path).readlines()
                # Filter lines that contain the specific string
                totens = [line for line in lines if " free  energy   TOTEN  = " in line]
                if totens:
                    # Take the last occurrence
                    last_line = totens[-1]
                    # Extract the value after '=' and strip whitespace
                    energy_value = last_line.split('=')[-1].strip()
                    # Append directory name and energy value to the results list
                    results.append((dirname, energy_value))
                else:
                    # No TOTEN line found
                    results.append((dirname, "TOTEN not found"))
            except:
                results.append((dirname, "Error reading OUTCAR"))
        else:
            # OUTCAR file not found
            results.append((dirname, "OUTCAR not found"))

# Print the results in table format
print("{:<30} {}".format("Folder", "Free energy TOTEN"))
print("-" * 50)
for entry in results:
    print("{:<30} {}".format(entry[0], entry[1]))
