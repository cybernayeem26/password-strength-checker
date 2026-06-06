import re
import tkinter as tk
from tkinter import ttk, messagebox


def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


def check_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return

    score = 0
    recommendations = []

    common_passwords = [
        "password",
        "123456",
        "admin",
        "qwerty",
        "welcome",
        "letmein"
    ]

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        recommendations.append("Use at least 8 characters")

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        recommendations.append("Add at least one uppercase letter")

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        recommendations.append("Add at least one lowercase letter")

    # Number Check
    if re.search(r"\d", password):
        score += 1
    else:
        recommendations.append("Add at least one number")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        recommendations.append("Add at least one special character")

    # Common Password Check
    if password.lower() in common_passwords:
        recommendations.append("Avoid commonly used passwords")

    # Repeated Character Check
    if re.search(r"(.)\1{2,}", password):
        recommendations.append("Avoid repeated characters")

    # Strength Rating
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score == 3:
        strength = "Medium"
        color = "orange"
    elif score == 4:
        strength = "Strong"
        color = "blue"
    else:
        strength = "Very Strong"
        color = "green"

    score_label.config(text=f"Score: {score}/5")
    strength_label.config(
        text=f"Strength: {strength}",
        fg=color
    )

    progress["value"] = score * 20

    recommendations_text.config(state="normal")
    recommendations_text.delete("1.0", tk.END)

    if recommendations:
        recommendations_text.insert(
            tk.END,
            "\n".join(f"• {item}" for item in recommendations)
        )
    else:
        recommendations_text.insert(
            tk.END,
            "Excellent! Your password follows strong security practices."
        )

    recommendations_text.config(state="disabled")


# Main Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("700x600")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="Password Strength Checker",
    font=("Arial", 22, "bold")
)
title_label.pack(pady=15)

# Password Label
password_label = tk.Label(
    root,
    text="Enter Password",
    font=("Arial", 12)
)
password_label.pack()

# Password Entry
password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14),
    show="*"
)
password_entry.pack(pady=10)

# Show Password Checkbox
show_password_var = tk.BooleanVar()

show_password_check = tk.Checkbutton(
    root,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password
)
show_password_check.pack()

# Button
check_button = tk.Button(
    root,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    command=check_password
)
check_button.pack(pady=15)

# Progress Bar
progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=350,
    mode="determinate"
)
progress.pack(pady=10)

# Score
score_label = tk.Label(
    root,
    text="Score: 0/5",
    font=("Arial", 12, "bold")
)
score_label.pack()

# Strength
strength_label = tk.Label(
    root,
    text="Strength: ",
    font=("Arial", 14, "bold")
)
strength_label.pack(pady=5)

# Recommendation Title
recommendation_label = tk.Label(
    root,
    text="Recommendations",
    font=("Arial", 14, "bold")
)
recommendation_label.pack(pady=10)

# Recommendation Box
recommendations_text = tk.Text(
    root,
    height=10,
    width=70
)
recommendations_text.pack()

recommendations_text.config(state="disabled")

# Footer
footer = tk.Label(
    root,
    text="Developed by Nayeem Ahmed | Cybersecurity Portfolio Project",
    font=("Arial", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()