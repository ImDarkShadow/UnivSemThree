import os
import cv2
import subprocess
# Define the folder path and file extension to look for
folder_path = "code"
file_extension = ".py"
output_path = "output"

# Define the LaTeX document preamble
document_preamble = r"""
\documentclass[a4paper,8pt]{article}
\usepackage{graphicx}
\usepackage[margin=0.5in,top=0.5in,bottom=0.5in,left=0.75in]{geometry}
\usepackage{fancyhdr} % for custom headers and footers
\pagestyle{fancy} % set page style to fancy
\renewcommand{\headrulewidth}{0pt}
\fancyhf{} % clear default header and footer
\fancyfoot[C]{\thepage} % set center of footer to be the page number
\usepackage{float}
\begin{document}
"""

# Define the LaTeX document body
document_body = ""

# Loop through all files in the folder with the specified file extension
for file_name in os.listdir(folder_path):
    if file_name.endswith(file_extension):
        with open(os.path.join(folder_path, file_name), "r") as f:
            python_code = f.read()
        # Define the input and output image names
        input_image_name = "input1.pgm"
        output_image_name = file_name.replace(".py", "_output.pgm")
        # Run the Python code with the input and output image names
        subprocess.call(["python3", os.path.join(
            folder_path, file_name), input_image_name, "output/"+output_image_name])
        # Create the output image
        # Add the Python code to the LaTeX document
        document_body += r"""
        \section{""" + file_name.replace(".py", "") + r"""}
        \begin{verbatim}
        """ + python_code + r"""
        \end{verbatim}
        """
        # Generate input and output image filenames
        input_image_filename = "input1.jpg"
        output_image_filename = file_name.replace(
            file_extension, "") + "_output.png"
        # Add the input and output images to the LaTeX document
        document_body += r"""
        \begin{figure}[H]
        \centering
        \begin{minipage}{0.4\linewidth}
        \centering
        \includegraphics[width=\linewidth]{""" + os.path.join(output_path, input_image_filename) + r"""}
        \caption{Input}
        \end{minipage}
        \hfill
        \begin{minipage}{0.4\linewidth}
        \centering
        \includegraphics[width=\linewidth]{""" + os.path.join(output_path, output_image_filename) + r"""}
        \caption{Output}
        \end{minipage}
        \end{figure}
        \clearpage
        """

# Define the LaTeX document postamble
document_postamble = r"""
\end{document}
"""

# Combine the preamble, body, and postamble into a complete LaTeX document
document = document_preamble + document_body + document_postamble

# Write the LaTeX document to a file
with open("output.tex", "w") as f:
    f.write(document)




# Compile the LaTeX document to generate the PDF output file
#os.system("pdflatex -output-directory=" + "output.tex")
