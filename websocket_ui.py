import tkinter as tk
from websockets.sync.client import connect

def start_communication():
    output_text.delete(1.0, tk.END)  # Clear the text box before starting
    with connect("ws://localhost:8765") as websocket:
        for i in range(1, 101):  # Display only first 100 interactions
            websocket.send("Request [" + str(i) + "] Hello world!")
            message = websocket.recv()
            output_text.insert(tk.END, f"Received: {message}\n")

# Create the main window
root = tk.Tk()
root.title("WebSocket Client")
root.geometry("750x550")
root.config(bg="#2C3E50")  # Dark background

# Create a colorful gradient-like header
header_frame = tk.Frame(root, bg="#34495E", height=50)
header_frame.pack(fill="x")
header_label = tk.Label(header_frame, text="WebSocket Client", font=("Helvetica", 24, "bold"), bg="#1ABC9C", fg="white")
header_label.pack(pady=10)

# Create a colorful button to start communication
start_button = tk.Button(
    root, text="Start Communication", command=start_communication,
    bg="#3498DB", fg="white", activebackground="#2980B9", font=("Helvetica", 14, "bold"), padx=10, pady=5, relief="raised", bd=3
)
start_button.pack(pady=20)

# Create a text box to display the communication log with gradient colors
output_text = tk.Text(root, height=20, width=80, bg="#ECF0F1", fg="#2C3E50", font=("Courier", 12), bd=5, relief="sunken")
output_text.pack(pady=10, padx=20)

# Add a scroll bar for the text box
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_text.yview)

# Customize the status label with gradient colors
status_frame = tk.Frame(root, bg="#2C3E50")
status_frame.pack(fill="x", pady=10)

status_label = tk.Label(status_frame, text="Ready to start WebSocket communication", bg="#2ECC71", fg="white", font=("Helvetica", 12, "italic"), padx=10, pady=5)
status_label.pack(side="left")

# Footer label for decorative purpose
footer_label = tk.Label(root, text="WebSocket Client UI - Enhanced Version", font=("Helvetica", 10), bg="#34495E", fg="white")
footer_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
