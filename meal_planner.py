# Core dependencies
import json
import os

import customtkinter as ctk
from PIL import Image

# Global UI theme configuration
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MealPlannerApp(ctk.CTk):
    # Main application class for the Meal Planner
    def __init__(self):
        super().__init__()

        # Window geometry and properties
        self.title("Budget Bytes 2026")
        self.width = 950
        self.height = 750
        self.center_window()

        # Database initialization
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            json_path = os.path.join(script_dir, "meals.json")
            with open(json_path, "r", encoding="utf-8") as file:
                self.meals_db = json.load(file)
            self.load_error = None
        except FileNotFoundError:
            self.meals_db = []
            self.load_error = "Error: 'meals.json' not found.\nCheck project folder."

        # Main grid layout configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar frame setup
        self.sidebar = ctk.CTkFrame(
            self, width=200, corner_radius=0, fg_color="#1a1a1a"
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        # Application branding/logo
        self.logo = ctk.CTkLabel(
            self.sidebar, text="BUDGET\nBYTES", font=ctk.CTkFont(size=22, weight="bold")
        )
        self.logo.grid(row=0, column=0, padx=20, pady=(30, 40))

        # Budget input controls
        self.budget_entry = ctk.CTkEntry(
            self.sidebar, placeholder_text="Budget £", width=140, height=35
        )
        self.budget_entry.grid(row=1, column=0, padx=20, pady=(0, 10))
        self.budget_entry.bind("<Return>", self.find_meals)

        # Search trigger button
        self.search_btn = ctk.CTkButton(
            self.sidebar,
            text="Find Meals",
            command=self.find_meals,
            height=35,
            font=ctk.CTkFont(weight="bold"),
        )
        self.search_btn.grid(row=2, column=0, padx=20, pady=5)

        # Metadata section header
        self.shop_label = ctk.CTkLabel(
            self.sidebar,
            text="PRICE SOURCES:",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#777777",
        )
        self.shop_label.grid(row=3, column=0, padx=20, pady=(30, 5), sticky="w")

        # Dynamic shop list generation from database
        shops = list(set([m["shop"] for m in self.meals_db])) if self.meals_db else []
        shops.sort()

        self.shop_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.shop_frame.grid(row=4, column=0, padx=20, sticky="w")

        for name in shops:
            lbl = ctk.CTkLabel(
                self.shop_frame,
                text=f" • {name} ",
                font=ctk.CTkFont(size=12),
                text_color="#aaaaaa",
            )
            lbl.pack(anchor="w")

        # Sidebar status footer
        self.status_lbl = ctk.CTkLabel(
            self.sidebar,
            text="Updated Apr 2026.\nEstimated Prices.",
            font=ctk.CTkFont(size=10),
            text_color="gray",
        )
        self.status_lbl.grid(row=5, column=0, pady=40)

        # Main scrollable content area
        self.scrollable_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scrollable_frame.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Global event bindings for scrolling
        self.bind_all("<MouseWheel>", self._on_mousewheel)  # Windows & macOS
        self.bind_all("<Button-4>", self._on_mousewheel)  # Linux (Scroll Up)
        self.bind_all("<Button-5>", self._on_mousewheel)  # Linux (Scroll Down)

        # Show initial welcome screen
        self.show_welcome_screen()

    def show_welcome_screen(self):
        # Displays a logo and welcome text in the main area on startup
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Image logo.png filename
            image_path = os.path.join(script_dir, "logo.png")

            # Open the image and convert it to RGBA mode to support transparency
            img = Image.open(image_path).convert("RGBA")  # type: ignore

            # Identify the background color (sampling the top-left pixel)
            datas = img.get_flattened_data()
            bg_color = datas[0]
            new_data = []

            for item in datas:
                # If the pixel color (40) of the background, makes it transparent
                if all(abs(item[i] - bg_color[i]) < 40 for i in range(3)):
                    new_data.append(
                        (255, 255, 255, 0)
                    )  # Replace with transparent white
                else:
                    new_data.append(item)

            img.putdata(new_data)

            self.welcome_logo = ctk.CTkImage(
                light_image=img,
                dark_image=img,
                size=(500, 500),  # Logo image size
            )

            self.logo_display = ctk.CTkLabel(
                self.scrollable_frame, image=self.welcome_logo, text=""
            )
            self.logo_display.pack(pady=(100, 20), fill="x", expand=True)

            ctk.CTkLabel(
                self.scrollable_frame,
                text="Welcome to Budget Bytes 2026\nEnter your budget to start planning!",
                font=ctk.CTkFont(size=16, slant="italic"),
                text_color="#777777",
            ).pack(fill="x", expand=True)
        except Exception:
            # Fallback if image is missing
            ctk.CTkLabel(
                self.scrollable_frame,
                text="BUDGET BYTES",
                font=ctk.CTkFont(size=40, weight="bold"),
                text_color="#333333",
            ).pack(pady=150, fill="x", expand=True)

    def _on_mousewheel(self, event):
        # Cross-platform mousewheel event handler
        try:
            if event.delta:
                scroll_amount = int(-1 * (event.delta / 120))
                self.scrollable_frame._parent_canvas.yview_scroll(
                    scroll_amount, "units"
                )
            elif event.num == 4:
                self.scrollable_frame._parent_canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.scrollable_frame._parent_canvas.yview_scroll(1, "units")
        except Exception:
            pass

    def center_window(self):
        # Calculate and set window position to screen center
        sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (sw // 2) - (self.width // 2), (sh // 2) - (self.height // 2)
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def find_meals(self, event=None):
        # Logic to filter and display meals based on budget
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if self.load_error:
            ctk.CTkLabel(
                self.scrollable_frame, text=self.load_error, text_color="#ff5555"
            ).pack(pady=20)
            return

        try:
            val = self.budget_entry.get().replace("£", "")
            budget = float(val)
        except ValueError:
            ctk.CTkLabel(
                self.scrollable_frame, text="Please enter a numeric budget. "
            ).pack(pady=20)
            return

        matches = sorted(
            [m for m in self.meals_db if m["cost"] <= budget], key=lambda x: x["cost"]
        )

        if not matches:
            ctk.CTkLabel(
                self.scrollable_frame, text="Try a slightly higher budget! "
            ).pack(pady=20)
        else:
            for m in matches:
                self.create_card(m)

    def create_card(self, m):
        # Factory method to build UI cards for individual meals
        card = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=8,
            border_width=1,
            border_color="#333333",
        )
        card.pack(fill="x", padx=10, pady=8)

        header = ctk.CTkLabel(
            card,
            text=f"{m['name']}  •  £{m['cost']:.2f} ",
            font=ctk.CTkFont(size=15, weight="bold"),
            text_color="#33ff33",
        )
        header.pack(anchor="w", padx=15, pady=(10, 2))

        shop = ctk.CTkLabel(
            card,
            text=f"Available at: {m['shop']} ",
            font=ctk.CTkFont(size=11, slant="italic"),
            text_color="#FFCC00",
        )
        shop.pack(anchor="w", padx=15)

        ctk.CTkLabel(
            card, text="SHOPPING LIST: ", font=ctk.CTkFont(size=11, weight="bold")
        ).pack(anchor="w", padx=15, pady=(8, 0))
        ctk.CTkLabel(
            card,
            text=f"{m['list']} ",
            wraplength=600,
            justify="left",
            text_color="#ADD8E6",
            font=ctk.CTkFont(size=12),
        ).pack(anchor="w", padx=15)

        if "breakdown" in m:
            ctk.CTkLabel(
                card, text="COST BREAKDOWN: ", font=ctk.CTkFont(size=11, weight="bold")
            ).pack(anchor="w", padx=15, pady=(8, 0))
            ctk.CTkLabel(
                card,
                text="\n".join(m["breakdown"]),
                justify="left",
                text_color="#aaaaaa",
                font=ctk.CTkFont(size=11),
            ).pack(anchor="w", padx=15)

        ctk.CTkLabel(
            card, text="COOKING INFO: ", font=ctk.CTkFont(size=11, weight="bold")
        ).pack(anchor="w", padx=15, pady=(8, 0))
        ctk.CTkLabel(
            card,
            text=f"{m['info']} ",
            wraplength=600,
            justify="left",
            font=ctk.CTkFont(size=12),
        ).pack(anchor="w", padx=15, pady=(0, 12))


# Application entry point
if __name__ == "__main__":
    app = MealPlannerApp()
    app.mainloop()
