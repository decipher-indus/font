import fontforge
import os

def merge_fonts(merge_font_path, base_font_path, output_path):
    base_font = fontforge.open(base_font_path)
    merge_font = fontforge.open(merge_font_path)

    base_font_glyphs = set(base_font)
    merge_font_glyphs = set(merge_font)

    # overlap = base_font_glyphs.intersection(merge_font_glyphs)
    # if overlap:
    #     print(f"Error: The following glyphs are present in both fonts: {overlap}")
    #     return
    new_family_name = "Indus Programmer"
    base_font.familyname = new_family_name
    base_font.fullname = f"{new_family_name} {base_font.fullname.partition('-')[2]}"
    base_font.fontname = f"{new_family_name.replace(' ', '')}-{base_font.fontname.partition('-')[2]}"

    base_font.mergeFonts(merge_font_path)

    base_font.generate(output_path)

    print(f"Fonts successfully merged and saved to {output_path}")

def merge_fonts_in_directory(base_dir, merge_font_path, output_dir):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(base_dir):
        if file_name.endswith(".ttf"):
            base_font_path = os.path.join(base_dir, file_name)
            output_path = os.path.join(output_dir, f'IndusProgrammer-{file_name.partition('-')[2]}')
            print(f"Merging {base_font_path} with {merge_font_path}...")
            merge_fonts(base_font_path, merge_font_path, output_path)


base_dir = "source-code-pro"  
merge_font_path = "IndusFont.ttf"  
output_dir = "IndusProgrammer"

merge_fonts_in_directory(base_dir, merge_font_path, output_dir)
