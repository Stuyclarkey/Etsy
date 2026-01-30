import tkinter as tk
from tkinter import ttk, messagebox
import random

class PresetPulseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PresetPulse - Etsy Listing Generator & Calculator")
        self.root.geometry("700x950")  # Increased height for calculator
        
        # --- Data: SEO Keywords (2025/2026 Trends) ---
        self.keywords = {
            "Boho / Warm": [
                "boho lightroom presets", "warm aesthetic", "beige presets", "creamy edit",
                "wedding photographer", "rustic filter", "lifestyle presets", "brown tones", 
                "instagram influencer", "golden hour", "earthy tones", "autumn aesthetic"
            ],
            "Dark & Moody": [
                "dark and moody", "cinematic presets", "black and white filter", "gothic aesthetic",
                "forest photography", "moody wedding", "desaturated tones", "shadow boost",
                "vsco filter", "film noir style", "dramatic edit", "night photography"
            ],
            "Bright & Airy": [
                "bright airy presets", "lightroom mobile", "clean aesthetic", "minimalist filter",
                "blogger essentials", "product photography", "white instagram theme", "soft pastel",
                "family portrait", "spring presets", "interior design", "glowing skin"
            ],
            "Film / Retro": [
                "film look presets", "kodak portra style", "grainy aesthetic", "retro 90s filter",
                "disposable camera", "vintage edit", "nostalgic vibes", "analog photography",
                "35mm film", "cinestill 800t", "classic film", "polaroid frame"
            ],
            "Cyberpunk / Neon": [
                "cyberpunk presets", "neon lights", "night city", "blue and teal",
                "urban photography", "futuristic edit", "streetwear aesthetic", "glow filter",
                "vibrant night", "tokyo style", "gaming aesthetic", "high contrast"
            ]
        }

        # ================= UI LAYOUT =================

        # --- Header ---
        tk.Label(root, text="PresetPulse Generator", font=("Arial", 18, "bold"), pady=10).pack()

        # --- Listing Generator Section ---
        frame_input = tk.LabelFrame(root, text="1. Create Listing", padx=20, pady=10, font=("Arial", 12, "bold"))
        frame_input.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_input, text="Preset Name:", font=("Arial", 10)).grid(row=0, column=0, sticky="w")
        self.entry_name = tk.Entry(frame_input, width=40)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame_input, text="Price ($):", font=("Arial", 10)).grid(row=1, column=0, sticky="w")
        self.entry_price = tk.Entry(frame_input, width=40)
        self.entry_price.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(frame_input, text="Select Vibe:", font=("Arial", 10)).grid(row=2, column=0, sticky="w")
        self.combo_vibe = ttk.Combobox(frame_input, values=list(self.keywords.keys()), width=37)
        self.combo_vibe.current(0)
        self.combo_vibe.grid(row=2, column=1, padx=10, pady=5)

        btn_generate = tk.Button(frame_input, text="Generate Text", command=self.generate_listing, bg="#007acc", fg="white", font=("Arial", 10, "bold"))
        btn_generate.grid(row=3, column=0, columnspan=2, pady=10)

        # --- Text Outputs ---
        frame_output = tk.Frame(root)
        frame_output.pack(fill="x", padx=20)

        tk.Label(frame_output, text="Title:", font=("Arial", 10, "bold")).pack(anchor="w")
        self.text_title = tk.Text(frame_output, height=2, width=80)
        self.text_title.pack(pady=2)

        tk.Label(frame_output, text="Description:", font=("Arial", 10, "bold")).pack(anchor="w")
        self.text_desc = tk.Text(frame_output, height=8, width=80)
        self.text_desc.pack(pady=2)

        tk.Label(frame_output, text="SEO Tags:", font=("Arial", 10, "bold")).pack(anchor="w")
        self.text_tags = tk.Text(frame_output, height=2, width=80)
        self.text_tags.pack(pady=2)

        # --- Profit Calculator Section ---
        frame_calc = tk.LabelFrame(root, text="2. Profit Calculator (Etsy Fees)", padx=20, pady=10, font=("Arial", 12, "bold"))
        frame_calc.pack(fill="x", padx=20, pady=20)

        # Labels for logic
        self.lbl_breakdown = tk.Label(frame_calc, text="Enter a price above and click Calculate", justify="left", font=("Courier", 10))
        self.lbl_breakdown.pack(side="left", padx=10)

        btn_calc = tk.Button(frame_calc, text="Calculate Profit", command=self.calculate_profit, bg="#28a745", fg="white", font=("Arial", 10, "bold"))
        btn_calc.pack(side="right", padx=10)

    # ================= LOGIC =================

    def generate_listing(self):
        name = self.entry_name.get()
        price = self.entry_price.get()
        vibe = self.combo_vibe.get()
        
        if not name or not price:
            messagebox.showerror("Error", "Please enter a Name and Price.")
            return

        # SEO & Text Logic
        main_kw = self.keywords[vibe][0]
        secondary_kw = self.keywords[vibe][1]
        title = f"{name} Lightroom Presets | {vibe} Preset Pack for Mobile & Desktop | {main_kw.title()}, {secondary_kw.title()}, Instagram Filter"
        
        desc = f"""🔥 TRANSFORM YOUR PHOTOS WITH {name.upper()}
Stop spending hours editing. Get that professional {vibe.lower()} look instantly.

✨ WHAT’S INCLUDED?
* Mobile Lightroom Presets (.DNG)
* Desktop Lightroom Presets (.XMP)
* PDF Installation Guide

👀 WHY CHOOSE THIS PACK?
* Perfect for: {vibe} photography & Instagram feeds.
* One-Click Magic: Designed for indoor and outdoor lighting.
* Fully Customizable.

💰 VALUE: Listed at ${price} (Compare to custom editing at $50/hour!)
"""
        vibe_tags = self.keywords[vibe]
        generic_tags = ["lightroom presets", "mobile presets", "photo filter", "digital download", "android ios"]
        all_tags = list(set(vibe_tags + generic_tags))
        random.shuffle(all_tags)
        final_tags = ", ".join(all_tags[:13])

        # Output to text boxes
        self.text_title.delete(1.0, tk.END)
        self.text_title.insert(tk.END, title)
        self.text_desc.delete(1.0, tk.END)
        self.text_desc.insert(tk.END, desc)
        self.text_tags.delete(1.0, tk.END)
        self.text_tags.insert(tk.END, final_tags)

    def calculate_profit(self):
        try:
            price_str = self.entry_price.get()
            if not price_str:
                messagebox.showerror("Error", "Please enter a Price first.")
                return
            
            revenue = float(price_str)
            
            # --- Etsy Fee Structure (2025/2026 Estimate) ---
            # 1. Listing Fee: $0.20 fixed
            fee_listing = 0.20
            
            # 2. Transaction Fee: 6.5% of sale price
            fee_transaction = revenue * 0.065
            
            # 3. Payment Processing (US Estimate): 3% + $0.25
            fee_processing = (revenue * 0.03) + 0.25
            
            total_fees = fee_listing + fee_transaction + fee_processing
            net_profit = revenue - total_fees
            margin = (net_profit / revenue) * 100

            # Display Result
            result_text = (
                f"Item Price:      ${revenue:.2f}\n"
                f"------------------------\n"
                f"Listing Fee:    -${fee_listing:.2f}\n"
                f"Transaction 6.5%:-${fee_transaction:.2f}\n"
                f"Processing 3%+.25:-${fee_processing:.2f}\n"
                f"------------------------\n"
                f"TOTAL FEES:      ${total_fees:.2f}\n"
                f"NET PROFIT:      ${net_profit:.2f} ({margin:.1f}%)"
            )
            self.lbl_breakdown.config(text=result_text, fg="black")

        except ValueError:
            messagebox.showerror("Error", "Price must be a number (e.g., 5.00)")

if __name__ == "__main__":
    root = tk.Tk()
    app = PresetPulseApp(root)
    root.mainloop()