import tkinter as tk
from tkinter import messagebox, Toplevel, Text, Scrollbar, RIGHT, Y, END
from models.map import Map
from helpers.read_csv import load_cities
import webbrowser
import os


def display_city_info():
    city_name = entry_city.get()
    city = city_map.find_city(city_name)
    if city:
        info = f"Country: {city.country}\nCity: {city.name}\nLongitude: {city.longitude}\nLatitude: {city.latitude}\nPopulation: {city.population}"
    else:
        info = "City not found."
    messagebox.showinfo("City Information", info)


def generate_city_map():
    city_name = entry_city.get()
    map_file_path = city_map.generate_city_map(city_name)
    if map_file_path:
        messagebox.showinfo(
            "Success", f"Map has been successfully created: {map_file_path}"
        )
        webbrowser.open("file://" + os.path.realpath(map_file_path))
    else:
        messagebox.showerror("Error", "City not found.")


def display_most_crowded():
    try:
        n = int(entry_n.get())
        sorted_cities = sorted(city_map.cities, key=lambda city: city.population, reverse=True)
        result = "\n".join([f"{i+1}. {city.name} - Population: {city.population}" for i, city in enumerate(sorted_cities[:n])])
        messagebox.showinfo(f"Top {n} Most Crowded Cities", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for N.")


def display_least_crowded():
    try:
        n = int(entry_n.get())
        sorted_cities = sorted(city_map.cities, key=lambda city: city.population)
        result = "\n".join([f"{i+1}. {city.name} - Population: {city.population}" for i, city in enumerate(sorted_cities[:n])])
        messagebox.showinfo(f"Top {n} Least Crowded Cities", result)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for N.")


def display_all_cities():
    result = "\n\n".join([f"Country: {city.country}\nCity: {city.name}\nLongitude: {city.longitude}\nLatitude: {city.latitude}\nPopulation: {city.population}" for city in city_map.cities])
    show_scrollable_message("All Cities", result)


def show_scrollable_message(title, message):
    top = Toplevel()
    top.title(title)

    text = Text(top, wrap="word")
    text.insert(END, message)
    text.config(state="disabled")
    text.pack(side="left", fill="both", expand=True)

    scrollbar = Scrollbar(top, command=text.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text.config(yscrollcommand=scrollbar.set)

    button = tk.Button(top, text="Close", command=top.destroy, bg="lightblue", font=("Helvetica", 12, "bold"))
    button.pack(pady=10)


def sort_cities_by_population():
    order = entry_order.get().upper()
    if order == "A":
        sorted_cities = sorted(city_map.cities, key=lambda city: city.population)
    elif order == "D":
        sorted_cities = sorted(city_map.cities, key=lambda city: city.population, reverse=True)
    else:
        messagebox.showerror("Error", "Please enter 'A' for ascending or 'D' for descending.")
        return

    result = "\n\n".join([f"{i+1}. {city.name} - Population: {city.population}" for i, city in enumerate(sorted_cities)])
    show_scrollable_message("Sorted Cities by Population", result)


# Load city data
city_map = Map()
city_map.cities = load_cities("./src/data/cleaned_germany_city_data.csv")

# Set up the main application window
root = tk.Tk()
root.title("City Population and Mapping System")

window_width = 700
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.configure(bg="#f0f0f0")

# Header
header_frame = tk.Frame(root, padx=20, pady=5, bg="darkblue")
header_frame.pack()

header_label = tk.Label(
    header_frame,
    text="City Population and Mapping System",
    font=("Helvetica", 18, "bold"),
    bg="darkblue",
    fg="white"
)
header_label.pack()

# Main frame for input fields
frame = tk.Frame(root, padx=20, pady=5, bg="#f0f0f0")
frame.pack(expand=True)

tk.Label(frame, text="Enter City Name:", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="black").grid(row=0, column=0, pady=5, sticky="e")
entry_city = tk.Entry(frame, width=30, font=("Helvetica", 12))
entry_city.grid(row=0, column=1, pady=5, padx=10)

tk.Label(frame, text="Enter N:", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="black").grid(row=1, column=0, pady=5, sticky="e")
entry_n = tk.Entry(frame, width=30, font=("Helvetica", 12))
entry_n.grid(row=1, column=1, pady=5, padx=10)

tk.Label(frame, text="Sort Order (A/D):", font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="black").grid(row=2, column=0, pady=5, sticky="e")
entry_order = tk.Entry(frame, width=30, font=("Helvetica", 12))
entry_order.grid(row=2, column=1, pady=5, padx=10)


# Button frame
button_frame = tk.Frame(root, padx=20, pady=5, bg="#f0f0f0")
button_frame.pack()

tk.Button(button_frame, text="Display City Info", command=display_city_info, width=20, bg="lightblue", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Generate City Map", command=generate_city_map, width=20, bg="lightgreen", font=("Helvetica", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)

tk.Button(button_frame, text="Display Most Crowded", command=display_most_crowded, width=20, bg="lightyellow", font=("Helvetica", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Display Least Crowded", command=display_least_crowded, width=20, bg="lightpink", font=("Helvetica", 12, "bold")).grid(row=1, column=1, padx=10, pady=5)

tk.Button(button_frame, text="Display All Cities", command=display_all_cities, width=20, bg="lightgray", font=("Helvetica", 12, "bold")).grid(row=2, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Sort Cities by Population", command=sort_cities_by_population, width=20, bg="lightcoral", font=("Helvetica", 12, "bold")).grid(row=2, column=1, padx=10, pady=5)

tk.Button(button_frame, text="Exit", command=root.quit, width=20, bg="lightblue", font=("Helvetica", 12, "bold")).grid(row=3, column=0, columnspan=2, pady=10)

# Start the application
root.mainloop()
