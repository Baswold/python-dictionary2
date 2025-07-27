import tkinter as tk
from tkinter import ttk, scrolledtext
import json
import re
import os

class PythonDictionaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Function Dictionary")
        self.root.geometry("900x700")
        self.root.configure(bg="#2d2d2d")
        
        self.data_file = "definitions.json"
        self.definitions = self.load_definitions()
        
        self.setup_ui()
    
    def load_definitions(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}
    
    def reload_definitions(self):
        self.definitions = self.load_definitions()
    
    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg="#2d2d2d")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        header_frame = tk.Frame(main_frame, bg="#2d2d2d", height=80)
        header_frame.pack(fill=tk.X, padx=20, pady=(20, 0))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="Python Function Dictionary", 
                              font=(".AppleSystemUIFont", 24, "bold"), 
                              fg="#ffffff", bg="#2d2d2d")
        title_label.pack(anchor=tk.W, pady=(10, 0))
        
        subtitle_label = tk.Label(header_frame, text="Type a word to look up in...", 
                                 font=(".AppleSystemUIFont", 14), 
                                 fg="#999999", bg="#2d2d2d")
        subtitle_label.pack(anchor=tk.W, pady=(5, 0))
        
        search_frame = tk.Frame(main_frame, bg="#2d2d2d")
        search_frame.pack(fill=tk.X, padx=20, pady=20)
        
        self.search_entry = tk.Entry(search_frame, font=(".AppleSystemUIFont", 16), 
                                    relief=tk.FLAT, bd=0, 
                                    highlightthickness=2, highlightcolor="#007AFF",
                                    highlightbackground="#555555",
                                    bg="#404040", fg="#ffffff", insertbackground="#ffffff")
        self.search_entry.pack(fill=tk.X, ipady=12)
        self.search_entry.bind('<Return>', lambda e: self.search_functions())
        self.search_entry.bind('<KeyRelease>', self.on_search_change)
        
        button_frame = tk.Frame(main_frame, bg="#2d2d2d")
        button_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        search_btn = tk.Button(button_frame, text="Search", command=self.search_functions,
                              font=(".AppleSystemUIFont", 14), bg="#007AFF", fg="white",
                              relief=tk.FLAT, bd=0, padx=20, pady=8,
                              activebackground="#0056CC", activeforeground="white")
        search_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        reload_btn = tk.Button(button_frame, text="Reload Definitions", command=self.reload_definitions,
                              font=(".AppleSystemUIFont", 14), bg="#555555", fg="white",
                              relief=tk.FLAT, bd=0, padx=20, pady=8,
                              activebackground="#777777", activeforeground="white")
        reload_btn.pack(side=tk.LEFT)
        
        self.results_frame = tk.Frame(main_frame, bg="#2d2d2d")
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        self.results_text = scrolledtext.ScrolledText(self.results_frame, 
                                                     font=(".AppleSystemUIFont", 12),
                                                     bg="#1e1e1e", fg="#ffffff",
                                                     relief=tk.FLAT, bd=0,
                                                     insertbackground="#ffffff",
                                                     selectbackground="#007AFF",
                                                     selectforeground="#ffffff")
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        self.show_welcome_message()
    
    def show_welcome_message(self):
        welcome_text = """Welcome to Python Function Dictionary!

To search for functions:
• Type a function name (e.g., 'append', 'len', 'split')
• Paste a code snippet to find all functions in it
• Press Enter or click Search

To add more functions:
• Edit the definitions.json file directly
• Click 'Reload Definitions' to refresh the database

Try searching for: append, len, split"""
        
        self.results_text.insert(tk.END, welcome_text)
        self.results_text.tag_add("welcome", "1.0", "end")
        self.results_text.tag_config("welcome", foreground="#cccccc", font=(".AppleSystemUIFont", 13))
    
    def on_search_change(self, event):
        search_text = self.search_entry.get().strip()
        if len(search_text) > 2:
            self.search_functions()
    
    def extract_function_names(self, text):
        all_matches = set()
        
        function_call_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        matches = re.findall(function_call_pattern, text)
        all_matches.update(matches)
        
        method_call_pattern = r'\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        dot_matches = re.findall(method_call_pattern, text)
        all_matches.update(dot_matches)
        
        single_word = text.strip()
        if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', single_word):
            all_matches.add(single_word)
        
        word_pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b'
        words = re.findall(word_pattern, text)
        for word in words:
            if word in self.definitions:
                all_matches.add(word)
        
        return list(all_matches)
    
    def search_functions(self):
        search_text = self.search_entry.get().strip()
        if not search_text:
            self.show_welcome_message()
            return
        
        function_names = self.extract_function_names(search_text)
        
        self.results_text.delete("1.0", tk.END)
        
        if not function_names:
            self.results_text.insert(tk.END, "No function names found in the input text.\n\n")
            self.results_text.insert(tk.END, "Try searching for function names like: append, len, split")
            return
        
        found_definitions = []
        missing_functions = []
        
        for func_name in function_names:
            if func_name in self.definitions:
                found_definitions.append(func_name)
            else:
                missing_functions.append(func_name)
        
        if found_definitions:
            for i, func_name in enumerate(found_definitions):
                definition_data = self.definitions[func_name]
                
                self.results_text.insert(tk.END, f"{func_name}\n", "function_name")
                self.results_text.insert(tk.END, "─" * 50 + "\n\n", "separator")
                
                definition = definition_data.get('definition', 'No definition available')
                self.results_text.insert(tk.END, f"{definition}\n\n", "definition")
                
                if definition_data.get('example'):
                    self.results_text.insert(tk.END, "Example:\n", "example_header")
                    self.results_text.insert(tk.END, f"{definition_data['example']}\n\n", "example")
                
                if i < len(found_definitions) - 1:
                    self.results_text.insert(tk.END, "\n" + "═" * 60 + "\n\n", "divider")
        
        if missing_functions:
            if found_definitions:
                self.results_text.insert(tk.END, "\n" + "═" * 60 + "\n\n", "divider")
            self.results_text.insert(tk.END, f"Functions not found: {', '.join(missing_functions)}\n", "missing")
            self.results_text.insert(tk.END, "Add them to definitions.json and click 'Reload Definitions'", "hint")
        
        self.results_text.tag_config("function_name", font=(".AppleSystemUIFont", 18, "bold"), foreground="#007AFF")
        self.results_text.tag_config("separator", foreground="#555555")
        self.results_text.tag_config("definition", font=(".AppleSystemUIFont", 13), foreground="#ffffff")
        self.results_text.tag_config("example_header", font=(".AppleSystemUIFont", 12, "bold"), foreground="#00D4AA")
        self.results_text.tag_config("example", font=("Monaco", 11), foreground="#ffcc99", background="#333333")
        self.results_text.tag_config("divider", foreground="#444444")
        self.results_text.tag_config("missing", foreground="#ff6b6b")
        self.results_text.tag_config("hint", foreground="#999999", font=(".AppleSystemUIFont", 11))
    

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonDictionaryApp(root)
    root.mainloop()