import os

# Directory containing the trace files
trace_directory = "traces/"
output_file = "experiments/lab4-prefetching.tlist"

# KNOBS constant value
knobs_value = "--knob_cloudsuite=true --warmup_instructions=100000000 --simulation_instructions=150000000"

# Get all filenames in the specified directory
trace_files = os.listdir(trace_directory)

# Open the output file and write entries for each trace file
with open(output_file, "w") as file:
        for trace in trace_files:
            file.write(f"NAME={trace}\n")
            file.write(f"TRACE=$(PYTHIA_HOME)/traces/{trace}\n")
            file.write(f"KNOBS={knobs_value}\n\n")

print(f"Created {output_file} with entries for traces in {trace_directory}.")
