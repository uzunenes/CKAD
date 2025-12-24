import re
import base64
import zlib
import os
import subprocess

def mermaid_to_kroki_url(mermaid_code):
    payload = zlib.compress(mermaid_code.encode('utf-8'), 9)
    encoded = base64.urlsafe_b64encode(payload).decode('utf-8')
    return f"https://kroki.io/mermaid/png/{encoded}"

def remove_emojis(text):
    emoji_pattern = re.compile(
        u'['
        u'\U0001F600-\U0001F64F'  # emoticons
        u'\U0001F300-\U0001F5FF'  # symbols & pictographs
        u'\U0001F680-\U0001F6FF'  # transport & map symbols
        u'\U0001F1E0-\U0001F1FF'  # flags (iOS)
        u'\U00002702-\U000027B0'
        u'\U000024C2-\U0001F251'
        u']+', flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def process_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace mermaid blocks
    def replace_mermaid(match):
        code = match.group(1).strip()
        url = mermaid_to_kroki_url(code)
        return f"\n![Mermaid Diagram]({url})\n"

    content = re.sub(r'```mermaid\n(.*?)\n```', replace_mermaid, content, flags=re.DOTALL)
    
    # Remove badges
    content = re.sub(r'!\[.*?\]\(https://img\.shields\.io/.*?\)', '', content)
    
    # Remove emojis
    content = remove_emojis(content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    input_md = 'pdf/CKAD-All-Labs.md'
    temp_md = 'pdf/CKAD-All-Labs-temp.md'
    output_pdf = 'pdf/CKAD-All-Labs.pdf'
    
    print("Processing Markdown...")
    process_markdown(input_md, temp_md)
    
    print("Generating PDF with Pandoc...")
    try:
        subprocess.run([
            'pandoc', temp_md, 
            '-o', output_pdf, 
            '--pdf-engine=xelatex', 
            '-V', 'mainfont=DejaVu Sans',
            '--toc',
            '--toc-depth=2',
            '-V', 'geometry:margin=1in'
        ], check=True)
        print(f"Successfully generated {output_pdf}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating PDF: {e}")
    finally:
        if os.path.exists(temp_md):
            os.remove(temp_md)

if __name__ == "__main__":
    main()
