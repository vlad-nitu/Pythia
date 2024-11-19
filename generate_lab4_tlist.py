import os

# Directory containing the trace files
trace_directory = "traces/"
output_file = "experiments/lab4-prefetching.tlist"

# KNOBS constant value

# Get all filenames in the specified directory
trace_files = os.listdir(trace_directory)

# Open the output file and write entries for each trace file
with open(output_file, "w") as file:
            for trace in trace_files:
                            # Extract the desired part of the trace name
                            trace_name = '.'.join(trace.split('.')[:2])
                            file.write(f"NAME={trace_name}\n")
                            file.write(f"TRACE=$(PYTHIA_HOME)/traces/{trace}\n")
                            file.write(f"KNOBS=\n")
            print(f"Created {output_file} with entries for traces in {trace_directory}.")
