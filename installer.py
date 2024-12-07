import os
import subprocess
from tqdm import tqdm
import sys

def run_command_with_progress(command):
    """Run a command while showing a progress bar"""
    # Create a tqdm progress bar with a total of 100 (for percentage completion)
    with tqdm(total=100, desc="Installing MediaMagic", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}]") as pbar:
        # Running the installation command in a subprocess
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Set the progress increment
        progress_increment = 10  # 10% per output line

        while True:
            # Read output and error streams line by line
            output = process.stdout.readline()
            error = process.stderr.readline()

            if output == '' and error == '' and process.poll() is not None:
                break  # Installation is complete

            if output:
                sys.stdout.write(output)  # Show output if needed
                pbar.update(progress_increment)  # Update progress bar by 10%

            if error:
                sys.stderr.write(error)  # Show error output if needed
                pbar.update(5)  # Smaller increment for errors

        process.wait()  # Wait for the process to finish

def display_stylish_message():
    """Display a stylish message for the user"""
    print("\n" + "="*50)
    print("\033[1;34m🔥 MediaMagic 🔥\033[0m")
    print("\033[1;33mCreated by: Codetech\033[0m")
    print("\033[1;32mGitHub: https://github.com/ShUBHaMJHA9/mediamagic\033[0m")
    print("="*50 + "\n")

def install_package():
    """Main function to handle the installation process"""
    display_stylish_message()  # Show stylish message before starting installation

    # Define the pip install command (editable installation)
    command = ["pip", "install", "-e", "."]

    # Run the command with progress bar
    run_command_with_progress(command)

    # Show completion message
    print("\n✅ Installation Complete! Thank you for using MediaMagic.\n")

if __name__ == "__main__":
    install_package()
